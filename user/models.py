from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField(blank=True)
    contact_no = models.CharField(max_length=30)

    def __str__(self):
        if self.user.first_name:
            return '{} {}'.format(
                self.user.first_name,
                self.user.last_name,
            )
        else:
            return self.user.username
