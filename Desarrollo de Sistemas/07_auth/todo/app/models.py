from django.db import models

# Create your models here.

class Task(models.Model):

    name = models.CharField('Task Name', max_length=64, null=False, blank=False)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.name