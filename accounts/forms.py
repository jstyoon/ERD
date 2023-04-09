from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']