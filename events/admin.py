from django.contrib import admin
from .models import Tournament, Team, Player  # Import your models

admin.site.register(Tournament)
admin.site.register(Team)
admin.site.register(Player)