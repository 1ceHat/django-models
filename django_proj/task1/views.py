from django.shortcuts import render
from .forms import UserRegister
from .models import *

# Create your views here.


def main_page(request):
    return render(request, 'main_page.html')


def shop_page(request):
    games = Game.objects.all()
    context = {
        'games': games,
    }
    return render(request, 'shop_page.html', context=context)


def basket_page(request):
    return render(request, 'basket_page.html')

def sign_up_by_django(request):
    users = Buyer.objects.all()
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if users.filter(name=username).exists():
                info.update({'error': 'Пользователь с таким именем существует!'})
            elif password != repeat_password:
                info.update({'error': 'Пароли не совпадают'})
            else:
                info.update({'message': f'Приветствуем, {username}'})
                Buyer.objects.create(name=username, age=age)
    else:
        form = UserRegister()
    info.update({'form': form})
    return render(request, 'registration_page.html', context={'info': info})