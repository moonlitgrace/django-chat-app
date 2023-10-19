from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from chat import views

urlpatterns = [
	path("", views.index, name="chat"),
	path("login/", LoginView.as_view(template_name="chat/login_page.html"), name="login"),
	path("logout/", LogoutView.as_view(), name="logout"),
]