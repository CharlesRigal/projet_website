from django.urls import path
from .views import index, projects, skills, detail_skill

urlpatterns = [
    path("", index, name="pf_index"),
    path("projets/", projects, name="projects"),
    path("skills/", skills, name="skills"),
    path("skill/<int:pk>", detail_skill, name="skill"),
]
