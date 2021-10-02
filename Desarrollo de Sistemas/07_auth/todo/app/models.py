from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):

    username = models.CharField(
        error_messages={
            'unique': _("dadasda"),
        },
    )
    colegio = models.CharField('Colegio', max_length=64, null=True, blank=True)
    nacionalidad = models.CharField('Nacionalidad', max_length=64, null=True, blank=True, default='Argentina')

    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'colegio', ]

class Task(models.Model):

    name = models.CharField('Task Name', max_length=64, null=False, blank=False)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.name