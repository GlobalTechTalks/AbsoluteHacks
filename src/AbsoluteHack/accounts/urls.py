from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path('login', auth_views.LoginView.as_view(template_name="accounts/login.html")),
    path('logout', auth_views.LogoutView.as_view(template_name="accounts/logout.html")),
    path('signup', views.SignUpView.as_view()),
]
