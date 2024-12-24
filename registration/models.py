# registration/models.py
from django.db import models

class Player(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    studio_associato = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username