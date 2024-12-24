
from .models import Player
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from django.contrib.auth.models import User

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Check if the username is already taken
        if User.objects.filter(username=username).exists():
            # Handle the case where the username is already taken
            return render(request, 'register1.html', {'error': 'Username already taken'})

        if password == confirm_password:
    # Create a new user account
          user = User.objects.create_user(username=username, password=password)
          user.save()
            # Redirect to a success page or perform any other actions
          return redirect('login')
        else:
            # Handle invalid password confirmation
            return render(request, 'register1.html')
    return render(request, 'register1.html')

def registerorg_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Check if the username is already taken
        if User.objects.filter(username=username).exists():
            # Handle the case where the username is already taken
            return render(request, 'register1org.html', {'error': 'Username already taken'})

        if password == confirm_password:
    # Create a new user account
          user = User.objects.create_user(username=username, password=password)
          user.save()
            # Redirect to a success page or perform any other actions
          return redirect('loginorg')
        else:
            # Handle invalid password confirmation
            return render(request, 'register1.html')
    return render(request, 'register1org.html')
def display_players(request):
    players = Player.objects.all()  # Fetch all players from the database
    return render(request, 'display_player.html', {'players': players})