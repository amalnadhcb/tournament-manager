from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'), 
    path('registerorg/', views.registerorg_view, name='registerorg'), # Update the view function name
    path('players/', views.display_players, name='display_players'),
]