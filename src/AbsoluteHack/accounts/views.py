from django.views import generic

from accounts.forms import SignUpForm


class SignUpView(generic.CreateView):
    template_name = "accounts/signup.html"
    form_class = SignUpForm
