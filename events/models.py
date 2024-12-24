# models.py
from django.db import models
from django.contrib.auth.models import User


class Tournament(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)  # Allow null temporarily
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True)  # Allow null temporarily
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True, related_name='members')
    game = models.CharField(max_length=100, null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name