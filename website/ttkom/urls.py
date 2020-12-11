from django.urls import path
from .views import index, post
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", index, name="index"),
    path("post/<int:pk>", post, name="post"),
    path("connextion/", auth_views.LoginView.as_view(), name="login"),
    path(
        "deconnection/",
        auth_views.LogoutView.as_view(template_name="registration/logged-out.html"),
        name="logout",
    ),
]
