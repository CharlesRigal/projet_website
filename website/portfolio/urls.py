from django.urls import path
from .views import index, projects, skills, detail_skill, detail_projet, cv, contact
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", index, name="pf_index"),
    path("projets/", projects, name="projects"),
    path("skills/", skills, name="skills"),
    path("skill/<int:pk>", detail_skill, name="skill"),
    path("projet/<int:pk>", detail_projet, name="projet"),
    path("cv/", cv, name="cv"),
    path("contact/", contact, name="contact"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
