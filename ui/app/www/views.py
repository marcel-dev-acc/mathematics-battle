from django.shortcuts import render
from math_battle.settings import DEBUG

if DEBUG == 0:
    BASE_URL = 'http://localhost:1350'
else:
    BASE_URL = 'http://localhost:3011'

# Create your views here.
def index(request):
    context = {
        'BASE_URL': BASE_URL
    }
    return render(request, 'main.html', context)

def game(request, session_id=None):
    context = {
        'BASE_URL': BASE_URL,
        'session_id': session_id,
    }
    return render(request, 'game.html', context)