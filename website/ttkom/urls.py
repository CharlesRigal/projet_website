from django.urls import path, reverse_lazy
from .views import index, post, register, activate, account_activation_send, DetailUser, like, account
from django.contrib.auth import views as auth_views

urlpatterns = [
    # edit account
    path("compte/", account, name="edit_account"),
    path("changer_le_mdp/", auth_views.PasswordChangeView.as_view(
        success_url=reverse_lazy("login"),
    ), name="password_change"),


    path("", index, name="index"),
    path("post/<int:pk>", post, name="post"),
    path("like/<int:pk>", like, name="like_post"),
    # login
    path("connextion/", auth_views.LoginView.as_view(), name="login"),
    path(
        "deconnection/",
        auth_views.LogoutView.as_view(template_name="registration/logged-out.html"),
        name="logout",
    ),
    # register
    path("inscription/", register, name="register"),
    path("activate/<str:uidb64>/<str:token>/", activate, name="activate"),
    path(
        "account_activation_sent/",
        account_activation_send,
        name="account_activation_send",
    ),
    # password recovery
    path(
        "reinitialiser-le-mot-de-pass/",
        auth_views.PasswordResetView.as_view(),
        name="password_reset",
    ),
    path(
        "reinitialiser-le-mot-de-pass/valider/",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reinitialiser/<str:uidb64>/<str:token>/",
        auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reinitialiser/valider/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    # look up user
    path("utilisateur/<int:pk>", DetailUser.as_view(), name="detail_user"),
]
