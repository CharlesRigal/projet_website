from django.shortcuts import render, get_object_or_404
from .models import Post
import django

# Create your views here.


def index(request):
    posts = Post.objects.filter(date_post__lt=django.utils.timezone.now()).order_by(
        "-date_post"
    )
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
