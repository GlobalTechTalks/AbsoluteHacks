from django.contrib.auth.forms import UserCreationForm

from users.models import User


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "college", "date_of_birth", "email")
