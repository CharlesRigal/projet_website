from django.shortcuts import render, get_object_or_404
from .models import Skill, Projet, Cv, Contact
from django.contrib.auth.models import User
from django.views.generic import DetailView
from .forms import ContactForm


def contact(request):
    send_form = ""
    form = ContactForm(request.POST or None)
    if request.POST and form.is_valid():
        Contact.objects.create(
            email=form.cleaned_data["email"],
            subject=form.cleaned_data["subject"],
            message=form.cleaned_data["message"],
        )

        admin = User.objects.get(username="rigal")
        admin.email_user(form.cleaned_data["subject"], form.cleaned_data["message"])
        form = ContactForm(None)
        send_form = "l'email a bien etait envoier"

    return render(
        request,
        "portfolio/contact.html",
        context={"form": form, "send_form": send_form},
    )


def cv(request):
    cv = get_object_or_404(Cv, pk=1)
    return render(request, "portfolio/cv.html", context={"cv": cv})


def index(request):
    return render(request, "portfolio/pf_index.html")


def projects(request):
    projets = Projet.objects.all()
    context = {"projets": projets}
    return render(request, "portfolio/pf_projects.html", context=context)


def skills(request):
    skills = Skill.objects.all()
    context = {"skills": skills}
    return render(request, "portfolio/pf_skills.html", context=context)


def detail_skill(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    projets = skill.projet_set.all()
    return render(
        request,
        "portfolio/skill_detail.html",
        context={"projets": projets, "skill": skill},
    )


def detail_projet(request, pk):
    projet = get_object_or_404(Projet, pk=pk)
    skills = projet.skills.all()
    return render(
        request,
        "portfolio/projet_detail.html",
        context={"projet": projet, "skills": skills},
    )
