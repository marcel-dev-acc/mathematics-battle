from django.shortcuts import render
import os

BASE_URL =os.environ.get("API_URL", default='http://localhost:3011')

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