from django.db import models
from user.models import Profile


class Student(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.profile)
