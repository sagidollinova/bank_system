import decimal
import urllib.parse

from django.shortcuts import render, redirect

from django.contrib.auth import logout

from BankSystem.forms import *
from Customer import utils
from Customer.models import *


def logout_view(request):
    logout(request)
    return redirect('/')


def profile(request):
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        username = request.session.get('username')
        cards = Card.objects.get(owner=username)
        usr = User.objects.get(nick=username)
        context = {'username': username,
                   'card_number': cards.cardNumber,
                   'expiration_date': cards.expirationDate,
                   'cvv': cards.cvv,
                   'kzt': cards.kzt,
                   'rub': cards.rub,
                   'usd': cards.usd,
                   'link': 'http://127.0.0.1:8000/' + str(usr.media_gallery)}
        return render(request, 'profile.html', context)


def transfer(request):
    username = request.session.get('username')
    if request.POST:
        data = {}
        raw_body = urllib.parse.unquote(request.body.decode("utf-8")).split('&')
        for pair in raw_body:
            elements = pair.split('=')
            data[elements[0]] = elements[1]
        amount = int(data['moneyAmount'])
        target = int(data['cardNumber'])
        cards = Card.objects.get(owner=username)
        context = {'kzt': cards.kzt,
                   'rub': cards.rub,
                   'usd': cards.usd,
                   'card_number': cards.cardNumber}

        if not Card.objects.filter(cardNumber=target).exists():
            context['error'] = 'Recipient card number was not found'
            return render(request, 'transfer.html', context)
        recipient = Card.objects.get(cardNumber=target)
        if data['currencyType'] == 'KZT':
            if cards.kzt >= amount:
                cards.kzt -= amount
                recipient.kzt += amount
            else:
                context['error'] = 'Not enough founds'
                return render(request, 'transfer.html', context)
        elif data['currencyType'] == 'RUB':
            if cards.rub >= amount:
                cards.rub -= amount
                recipient.rub += amount
            else:
                context['error'] = 'Not enough founds'
                return render(request, 'transfer.html', context)
        elif data['currencyType'] == 'USD':
            if cards.usd >= amount:
                cards.usd -= amount
                recipient.usd += amount
            else:
                context['error'] = 'Not enough founds'
                return render(request, 'transfer.html', context)
        cards.save()
        recipient.save()
        return redirect('/profile')

    else:
        cards = Card.objects.get(owner=username)
        context = {'kzt': cards.kzt,
                   'rub': cards.rub,
                   'usd': cards.usd,
                   'card_number': cards.cardNumber}
        return render(request, 'transfer.html', context)


def convert_money(request):
    username = request.session.get('username')
    if request.method == 'POST':
        data = {}
        raw_body = urllib.parse.unquote(request.body.decode("utf-8")).split('&')
        for pair in raw_body:
            elements = pair.split('=')
            data[elements[0]] = elements[1]
        # print(data)
        usd_kzt, rub_kzt, kzt_usd, kzt_rub, usd_rub, rub_usd = utils.getCurrency()
        amount = int(data['moneyAmount'])
        cards = Card.objects.get(owner=username)
        context = {'kzt': cards.kzt,
                   'rub': cards.rub,
                   'rub_currency': rub_kzt,
                   'usd': cards.usd,
                   'usd_currency': usd_kzt,
                   'currency': '',
                   'card_number': cards.cardNumber}
        if data['fromCurrencyType'] == 'KZT':
            if data['ToCurrencyType'] == 'USD':
                if cards.kzt >= amount * usd_kzt:
                    print('YEAH')
                    cards.kzt -= amount * decimal.Decimal(usd_kzt)
                    cards.usd += amount
                    cards.save()
                else:
                    context['error'] = 'Not enough money'
                    return render(request, 'convertMoney.html', context)
            elif data['ToCurrencyType'] == 'RUB':
                if cards.kzt >= amount * rub_kzt:
                    print('YEAH')
                    cards.kzt -= amount * decimal.Decimal(rub_kzt)
                    cards.usd += amount
                    cards.save()
                else:
                    context['error'] = 'Not enough money'
                    return render(request, 'convertMoney.html', context)
        elif data['fromCurrencyType'] == 'RUB':
            if data['ToCurrencyType'] == 'USD':
                if cards.rub >= amount * usd_rub:
                    print('YEAH')
                    cards.rub -= amount * decimal.Decimal(usd_rub)
                    cards.usd += amount
                    cards.save()
                else:
                    context['error'] = 'Not enough money'
                    return render(request, 'convertMoney.html', context)
            elif data['ToCurrencyType'] == 'KZT':
                if cards.rub >= amount * kzt_rub:
                    print('YEAH')
                    cards.rub -= amount * decimal.Decimal(kzt_rub)
                    cards.kzt += amount
                    cards.save()
                else:
                    context['error'] = 'Not enough money'
                    return render(request, 'convertMoney.html', context)
        elif data['fromCurrencyType'] == 'USD':
            if data['ToCurrencyType'] == 'KZT':
                if cards.usd >= amount * kzt_usd:
                    print('YEAH')
                    cards.usd -= amount * decimal.Decimal(kzt_usd)
                    cards.kzt += amount
                    cards.save()
                else:
                    context['error'] = 'Not enough money'
                    return render(request, 'convertMoney.html', context)
            elif data['ToCurrencyType'] == 'RUB':
                if cards.usd >= amount * rub_usd:
                    print('YEAH')
                    cards.usd -= amount * decimal.Decimal(rub_usd)
                    cards.rub += amount
                    cards.save()
                else:
                    context['error'] = 'Not enough money'
                    return render(request, 'convertMoney.html', context)
        return redirect('/profile')
    elif request.method == 'GET':
        username = request.session.get('username')
        usd_kzt, rub_kzt, kzt_usd, kzt_rub, usd_rub, rub_usd = utils.getCurrency()
        cards = Card.objects.get(owner=username)
        context = {'kzt': cards.kzt,
                   'rub': cards.rub,
                   'rub_currency': rub_kzt,
                   'usd': cards.usd,
                   'usd_currency': usd_kzt,
                   'currency': '',
                   'card_number': cards.cardNumber}
        return render(request, 'convertMoney.html', context)


def write_income(request):
    username = request.session.get('username')
    if request.method == 'POST':
        data = {}
        raw_body = urllib.parse.unquote(request.body.decode("utf-8")).split('&')
        for pair in raw_body:
            elements = pair.split('=')
            data[elements[0]] = elements[1]
        # print(data)
        amount = int(data['moneyAmount'])
        cards = Card.objects.get(owner=username)
        if data['currencyType'] == 'KZT':
            cards.kzt += amount
        elif data['currencyType'] == 'RUB':
            cards.rub += amount
        elif data['currencyType'] == 'USD':
            cards.usd += amount
        cards.save()
        return redirect('/profile')
    elif request.method == 'GET':
        username = request.session.get('username')
        cards = Card.objects.get(owner=username)
        context = {'kzt': cards.kzt,
                   'rub': cards.rub,
                   'usd': cards.usd,
                   'card_number': cards.cardNumber}
        return render(request, 'getMoney.html', context)


def change_password(request):
    username = request.session.get('username')
    form_new_pass = PasswordChangeForm()
    if request.POST:
        form = PasswordChangeForm(request.POST)
        if form.is_valid():
            p_1 = form.cleaned_data.get('password_1')
            p_2 = form.cleaned_data.get('password_2')
            if p_1 == p_2:
                if len(p_1) > 6:
                    usr = User.objects.get(nick=username)
                    usr.password = p_1
                    usr.save()
                    return redirect('/profile')
                else:
                    context = {'error': 'Password is too short', 'form': form_new_pass}
                    return render(request, 'changePass.html', context)
            else:
                context = {'error': 'Passwords are different', 'form': form_new_pass}
                return render(request, 'changePass.html', context)
    else:
        context = {'form': form_new_pass}
        return render(request, 'changePass.html', context)


def photo_upload(request):
    username = request.session.get('username')
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            with open(f'photos/{username}.jpg', 'wb+') as destination:
                for chunk in request.FILES['file'].chunks():
                    destination.write(chunk)
            usr = User.objects.get(nick=username)
            usr.media_gallery = f'photos/{username}.jpg'
            usr.save()
            pass
    else:
        form = UploadFileForm()
    return render(request, 'photo.html', {'form': form})