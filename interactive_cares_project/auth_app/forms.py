from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from auth_app import models

# Create your forms here.

class SignupForm(UserCreationForm):
    class Meta:
        model = models.User
        fields = ("email", "username", "password1", "password2",)

class EditProfileForm(UserChangeForm):
    class Meta:
        model = models.User
        fields = ("email", "username", "full_name", "phone_number", "bio", "profile_picture", "password",)
