from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterFrom
from django.contrib.auth.models import User



def register(request):
    if request.method == 'POST':
        form = UserRegisterFrom(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Аккаунт {username} создан!')
            return redirect('login')
    else:
        form = UserRegisterFrom
    return render(request, 'users/register.html', {'form':form})

def profile(request):
    User_date = request.user
    data = {
        "title":"Личный кабинет",
        "user":User_date
    }
    return render(request, 'users/profile.html', data)
