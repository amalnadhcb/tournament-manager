from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Tournament, Team, Player,PlayerRegistration

def home(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('tournament_dashboard')  # Redirect to the tournament dashboard page
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        name = request.POST['name']
        email = request.POST['email']
        age = request.POST['age']
        game = request.POST['game']
        weight = request.POST['weight']
        category = request.POST['category']

        # Create a new player instance and save it to the database
        player = Player.objects.create(
            username=username,
            password=password,
            name=name,
            email=email,
            age=age,
            game=game,
            weight=weight,
            category=category
        )
        player.save()

        # Login the player
        login(request, player)
        return redirect('tournament_dashboard')

@login_required
def player_profile(request):
    try:
        player = request.user.player
    except Player.DoesNotExist:
        messages.error(request, 'You do not have a player profile. Please register as a player.')
        return redirect('register')
    return render(request, 'player_profile.html', {'player': player})

def tournament_dashboard(request):
    tournaments = Tournament.objects.all()
    return render(request, 'tournament_dashboard.html', {'tournaments': tournaments})

def team_profile(request, team_id):
    try:
        team = Team.objects.get(id=team_id)
    except Team.DoesNotExist:
        messages.error(request, 'Team not found.')
        return redirect('tournament_dashboard')
    return render(request, 'team_profile.html', {'team': team})

def logout_view(request):
    logout(request)
    return redirect('login')

def contact_us(request):
    return render(request, 'contact_us.html')

def info(request):
    return render(request, 'info.html')

def fixtures(request):
    return render(request, 'fixtures.html')

def results(request):
    return render(request, 'results.html')



# In your views.py file
def organizer_dashboard(request):
    tournaments = Tournament.objects.all()  # Fetch all tournaments
    return render(request, 'organizer_dashboard.html', {'tournaments': tournaments})

from .forms import TournamentForm

def add_tournament(request):
    if request.method == 'POST':
        form = TournamentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('organizer_dashboard')  # Redirect to the tournament dashboard
    else:
        form = TournamentForm()
    return render(request, 'add_tournament.html', {'form': form})

def loginorg_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('organizer_dashboard')  # Redirect to the tournament dashboard page
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

from django.shortcuts import render, redirect
from .models import Tournament  # Assuming you have a Tournament model

def submit_tournament(request):
    if request.method == 'POST':
        name = request.POST['name']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        # Create a new tournament instance and save it
        tournament = Tournament(name=name, start_date=start_date, end_date=end_date)
        tournament.save()
        return redirect('organizer_dashboard')  # Redirect to the dashboard or another page
    return render(request, 'add_tournament.html')  # Render the form if not a POST request

# events/views.py
from django.shortcuts import render, get_object_or_404
from .models import Tournament  # Assuming you have a Tournament model

def tournament_detail(request, id):
    tournament = get_object_or_404(Tournament, id=id)
    return render(request, 'tournament_detail.html', {'tournament': tournament})


def results_view(request):
    # Your logic here
    return render(request, 'results.html')


def registered_players(request):
    players = PlayerRegistration.objects.all()
    return render(request, 'registered_players.html', {'players': players})

from .models import Tournament
from django.views.decorators.csrf import csrf_protect

@csrf_protect
        

def tournament_registration(request):
    try:
        player = request.user.player
    except Player.DoesNotExist:
        player = Player.objects.create(user=request.user)
        player.save()

    # Populate the player object with the user's data
    player.name = request.user.username
    player.email = request.user.email
    # Add other fields as needed

    tournament_id = request.POST.get('tournament_id')
    if tournament_id:
        tournament = Tournament.objects.get(id=tournament_id)
        if request.method == 'POST':
            # Handle the form submission
            player_name = request.POST['name']
            player_email = request.POST['email']
            player_age = request.POST['age']
            player_weight_category = request.POST['weight-category']

            # Create a new PlayerRegistration instance and save it to the database
            player_registration = PlayerRegistration.objects.create(
                tournament=tournament,
                player_name=player_name,
                player_email=player_email,
                player_age=player_age,
                player_weight_category=player_weight_category
            )
            player_registration.save()

            # Return a redirect response to the tournament dashboard page
            return redirect('tournament_dashboard')
        else:
            # Return the tournament registration form
            return render(request, 'tournament_registration.html', {
                'tournament': tournament,
                'player': player
            })
    else:
        # Return the tournament registration form
        return render(request, 'tournament_registration.html')
    
def registered_players(request):
    tournament_id = request.GET.get('tournament_id')
    if tournament_id:
        tournament = Tournament.objects.get(id=tournament_id)
        players = PlayerRegistration.objects.filter(tournament=tournament)
        return render(request, 'registered_players.html', {'players': players})
    else:
        return render(request, 'registered_players.html', {'players': PlayerRegistration.objects.all()})


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def player_profile(request):
    user = request.user
    return render(request, 'player_profile.html', {'user': user})







import random
import math
from django.shortcuts import render

def get_player_data(players):
    return [{'name': player.player_name, 'email': player.player_email, 'age': player.player_age, 'weight_category': player.player_weight_category} for player in players]

import random

def generate_knockout_fixtures(players):
    num_players = len(players)
    if num_players < 2:
        raise ValueError("Not enough players to generate a knockout fixture")

    # Shuffle the players to randomize the order
    random.shuffle(players)

    # Create a list to store the fixtures
    fixtures = []

    # Loop through the players and create fixtures
    while len(players) > 1:
        round_fixtures = []
        for i in range(len(players) // 2):
            player1 = players[i]
            player2 = players[len(players) - i - 1]
            round_fixtures.append((player1, player2))
        fixtures.append(round_fixtures)
        # Update the players list for the next round
        players = [player1 for player1, player2 in round_fixtures]

    return fixtures

def fixtures(request):
    players = PlayerRegistration.objects.all()
    player_data = [{'name': player.player_name, 'email': player.player_email} for player in players]
    try:
        knockout_fixtures = generate_knockout_fixtures(player_data)
    except ValueError as e:
        return render(request, 'fixtures.html', {'error': str(e)})

    return render(request, 'fixtures.html', {'knockout_fixtures': knockout_fixtures})

def generate_fixtures(request, tournament_id):
    tournament = Tournament.objects.get(id=tournament_id)
    players = PlayerRegistration.objects.filter(tournament=tournament)
    player_data = [{'name': player.player_name, 'email': player.player_email} for player in players]
    try:
        knockout_fixtures = generate_knockout_fixtures(player_data)
    except ValueError as e:
        return render(request, 'fixtures.html', {'error': str(e)})

    return render(request, 'fixtures.html', {'knockout_fixtures': knockout_fixtures})

# events/views.py
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

@require_http_methods(['POST'])
def update_winner(request):
    winner = request.POST.get('winner')
    match = request.POST.get('match')
    # Update the winner in the database
    # ...
    # Generate the updated Round 2 matches
    round2_matches = generateRound2Matches(winner)
    return HttpResponse(round2_matches)

def generateRound2Matches(winner):
    # Generate the updated Round 2 matches based on the winner
    # ...
    return '<li>' + winner + ' vs TBD</li>'
    
