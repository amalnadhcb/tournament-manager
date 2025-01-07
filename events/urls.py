from django.urls import path
from . import views
from .views import register, login_view, logout_view, player_profile,submit_tournament,tournament_detail
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('loginorg/', views.loginorg_view, name='loginorg'),
    path('profile/', player_profile, name='player_profile'),  # This should match the login redirect
    path('contact/', views.contact_us, name='contact_us'),
    path('info/', views.info, name='info'),
    path('dashboard/', views.tournament_dashboard, name='tournament_dashboard'),
    path('dashboard2/', views.organizer_dashboard, name='organizer_dashboard'),
        path('add_tournament/', views.add_tournament, name='add_tournament'),
        path('submit-tournament/', submit_tournament, name='submit_tournament'),
        path('tournament/<int:id>/', tournament_detail, name='tournament_detail'),
    path('fixtures/', views.fixtures, name='fixtures'),
    path('results/', views.results_view, name='results'),
    path('team/<int:team_id>/', views.team_profile, name='team_profile'),
    path('logout/', logout_view, name='logout'),
    path('tournament/registration/', views.tournament_registration, name='tournament_registration'),
    path('registered-players/', views.registered_players, name='registered_players'),
]


# events/urls.py

