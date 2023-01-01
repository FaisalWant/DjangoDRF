from django.contrib.auth.views import (
	LoginView, 
	LogoutView, 
	PasswordChangeDoneView,
	PasswordChangeView 
	)


from django.contrib.auth.decorators import login_required 

from django.urls import path, reverse_lazy
from django.views.generic import TemplateView 

urlpatterns=[
	path("account/", login_required(TemplateView.as_view(template_name="user/account.html")),name="account")
	path("login/", LoginView.as_view(template_name="user/login.html"), name="login"),
	path("logout/",LogoutView.as_view(template_name="user/logout.html"), name="logout"),
	path(
		"password_change", PasswordChangeView.as_view(success_url=reverse_lazy("auth:password_change_done")),
		name="password_change",), 
	path("password_change/done/", PasswordChangeDoneView.as_view(), name="password_change_done",
		),
	]