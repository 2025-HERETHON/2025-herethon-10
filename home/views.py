# home/views.py
from django.shortcuts import redirect, render

def root_redirect(request):
    return redirect('/accounts/signup/')

def home_view(request):
    if not request.user.is_authenticated:
        return redirect('/user/login/')  
    return render(request, 'home.html', {
        'user': request.user,
    })
