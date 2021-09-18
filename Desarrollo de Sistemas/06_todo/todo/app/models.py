from django.db import models

# Create your models here.

class Task(models.Model):

    description = models.CharField('Task Description', max_length=256)
    done = models.BooleanField('Is Done')

    def __str__(self):
        return f"{self.description | {self.done}}"