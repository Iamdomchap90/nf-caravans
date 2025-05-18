from django.contrib.auth import views as auth
from django.urls import path

urlpatterns = [
    path(
        "reset-password/",
        auth.PasswordResetView.as_view(),
        name="admin_password_reset",
    ),
    path("reset-password/done/", auth.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path(
        "reset-password/<uidb64>/<token>/",
        auth.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset-password/complete/",
        auth.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
]
