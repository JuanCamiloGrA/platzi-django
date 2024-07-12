from django.urls import path
from django.contrib.auth.views import LoginView
from .views import RegisterView, logout_view

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
]
