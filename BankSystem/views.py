import datetime
import random

from django.shortcuts import render, redirect

from Customer.models import *
from BankSystem.forms import *


def login(request):
    if request.session.get('username') is not None:
        return redirect('/profile')
    form_send = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            usr_name = form.cleaned_data.get('username')
            passw = form.cleaned_data.get('password')
            if User.objects.filter(nick=usr_name).exists():
                u = User.objects.get(nick=usr_name)
                if u.password == passw:
                    request.session['username'] = usr_name
                    return redirect('/profile')
                else:
                    context = {'error': 'Invalid username or password', 'form': form_send}
                    return render(request, 'login.html', context)
            else:
                context = {'error': 'Invalid username or password', 'form': form_send}
                return render(request, 'login.html', context)
    elif request.method == 'GET':
        context = {'form': form_send}
        return render(request, 'login.html', context)


def register(request):
    if request.session.get('username') is not None:
        return redirect('/profile')
    form_send = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            e = form.cleaned_data.get('email')
            u = form.cleaned_data.get('username')
            if len(u) < 6:
                context = {'error': 'Username is too short', 'form': form_send}
                return render(request, 'register.html', context)
            p = form.cleaned_data.get('password')
            if len(p) < 6:
                context = {'error': 'Password is too short', 'form': form_send}
                return render(request, 'register.html', context)

            if User.objects.filter(nick=u).exists() or User.objects.filter(email=e).exists():
                context = {'error': 'Username or email is already taken', 'form': form_send}
                return render(request, 'register.html', context)
            else:
                usr = User(nick=u, password=p, email=e)
                usr.save()
                card_number = 54798216 * 100000000 + random.randint(10000000, 99999999)
                t = datetime.date.today()
                expiration_date = str(t.month) + '/' + str(t.year + 5)
                cvv = random.randint(100, 999)
                card = Card(cardNumber=card_number, expirationDate=expiration_date, cvv=cvv,
                            kzt=5000, rub=0, usd=0, owner=u)
                card.save()
                request.session['username'] = u
                return redirect('/profile')
    elif request.method == 'GET':
        context = {'form': form_send}
        return render(request, 'register.html', context)



