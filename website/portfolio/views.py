from django.shortcuts import render, get_object_or_404
from .models import Skill, Projet
from django.views.generic import DetailView


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
    return render(request, "portfolio/skill_detail.html", context={"projets": projets, "skill": skill})
