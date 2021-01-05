from django.shortcuts import render
from .models import Skill, Projet


def index(request):
    return render(request, "portfolio/pf_index.html")

def project(request):
    projets = Projet.objects.all()
    context = {'projets': projets}
    return render(request, "portfolio/pf_project.html",context=context)
