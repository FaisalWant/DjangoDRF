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

from django.urls import path, reverse_lazy,re_path
from django.views.generic import TemplateView 

from django_registration.backends.activation import (
    urls as registration_urls,
)
from django_registration.backends.activation.views import (
    RegistrationView,
    ActivationView
)

from .forms import RegistrationForm

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
		),
	path(
        "activate/complete/",
        TemplateView.as_view(
            template_name="django_registration/activation_complete.html"
        ),
        name="django_registration_activation_complete",
    ),
    re_path(
        r"^activate/(?P<activation_key>[-:\w]+)/$",
        ActivationView.as_view(
            success_url=reverse_lazy(
                "auth:django_registration_activation_complete"
            )
        ),
        name="django_registration_activate",
    ),
    path(
        "register/",
        RegistrationView.as_view(
            form_class=RegistrationForm,
            success_url=reverse_lazy(
                "auth:django_registration_complete"
            ),
        ),
        name="django_registration_register",
    ),
    path(
        "register/complete/",
        TemplateView.as_view(
            template_name="django_registration/registration_complete.html"
        ),
        name="django_registration_complete",
    ),
    path(
        "register/closed/",
        TemplateView.as_view(
            template_name="django_registration/registration_closed.html"
        ),
        name="django_registration_disallowed",
    ),

]