from django.shortcuts import render, redirect
from .forms import TournamentCreationForm

def tours_view(request):
    return render(request, 'tournaments/tours_main.html')

def create_tour(request):

    form = TournamentCreationForm(request.POST)

    return render(request, 'tournaments/create_tour.html', {'form': form})