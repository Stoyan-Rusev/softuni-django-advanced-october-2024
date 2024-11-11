from django.contrib.auth.forms import UserCreationForm

from forumApp.accounts.models import CustomUser


class UserCreateForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')
