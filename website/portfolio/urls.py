from django.urls import path
from .views import index, project

urlpatterns = [
    path("", index, name="pf_index"),
    path("projets/", project, name="projects"),
]
