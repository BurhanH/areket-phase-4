from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from . import models


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = models.CustomUser
        fields = ('username', 'email', 'age',)


class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = models.CustomUser
        fields = ('username', 'email', 'age',)
