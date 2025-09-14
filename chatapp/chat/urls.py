from django.urls import path
from django.contrib.auth import views as auth_views   # 👈 add this
from . import views

urlpatterns = [
    path("", views.home, name="home"),   # homepage
    path("chat/<str:room_name>/", views.room, name="room"),
    path("login/", auth_views.LoginView.as_view(template_name="chat/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),
]
