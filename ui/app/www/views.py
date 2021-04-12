from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    return render(request, 'main.html', context)

def game(request, session_id=None):
    context = {
        'session_id': session_id,
    }
    return render(request, 'game.html', context)