from django.contrib.auth.views import (
	LoginView, 
	LogoutView, 
	PasswordChangeDoneView,
	PasswordChangeView,
	PasswordResetView,
	PasswordResetConfirmView,
	AccountPage
		)


from django.contrib.auth.decorators import login_required 

from django.urls import path, reverse_lazy
from django.views.generic import TemplateView 

urlpatterns=[
	 path("account/", AccountPage.as_view(), name="account"), 
	path("login/", LoginView.as_view(template_name="user/login.html"), name="login"),
	path("logout/",LogoutView.as_view(template_name="user/logout.html"), name="logout"),
	path(
		"password_change", PasswordChangeView.as_view(success_url=reverse_lazy("auth:password_change_done")),
		name="password_change",), 

	path("password_change/done/", PasswordChangeDoneView.as_view(), name="password_change_done",
		),

	path("password_reset/", PasswordResetView.as_view(), name= "password_reset"),
	path("password_reset/<uidb64>/<token>/", PasswordResetConfirmView.as_view(), name="password_reset_confirm",
		)
	]