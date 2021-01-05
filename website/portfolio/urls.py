from django.urls import path
from .views import index, project, skill

urlpatterns = [
    path("", index, name="pf_index"),
    path("projets/", project, name="projects"),
    path("skills/", skill, name="skills"),
]
