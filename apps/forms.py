from django.contrib.auth.forms import UserCreationForm
from django.db import models


class CustomForModel(UserCreationForm):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=155)
