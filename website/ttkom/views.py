from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, User
from .forms import RegisterForm
from django.utils import timezone
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import login
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from .tokens import account_activation_token

# Create your views here.

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('index')
    else:
        return render(request, 'registration/account_activation_invalid.html')


def register(request):
    form = RegisterForm(request.POST or None)
    print(request.POST)

    if request.POST and form.is_valid():
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        current_site = get_current_site(request)
        subject = "Activer votre compte"
        message = render_to_string(
            "registration/account_activation_email.html",
            {
                "user": user,
                "domain": current_site.domain,
                "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                "token": account_activation_token.make_token(user),
            },
        )
        user.email_user(subject, message)
        return redirect('account_activation_send')
    context = {"form": form}
    return render(request, "registration/register.html", context=context)

def account_activation_send(request):
    return render(request, "registration/account_activation_send.html")

def index(request):
    posts = Post.objects.filter(date_post__lt=timezone.now()).order_by("-date_post")
    data = {
        "posts": posts,
    }
    return render(request, "ttkom/index.html", context=data)


def post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    data = {
        "post": post,
    }
    return render(request, "ttkom/post.html", context=data)
