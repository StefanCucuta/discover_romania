from django.db import models
from django.contrib.auth.models import User


class Wish(models.Model):
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.item + ' | ' + str(self.completed)
