from django.shortcuts import render
from .forms import UserRegister
from django.core.paginator import Paginator
from .models import *

# Create your views here.


def main_page(request):
    return render(request, 'main_page.html')


def shop_page(request):
    obj_per_page = request.GET.get('el_on_page')
    games = Game.objects.all()
    paginator = Paginator(games, per_page=1 if obj_per_page is None else obj_per_page)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)

    context = {
        'games': games,
        'page_obj': page_obj,
        'obj_pp': obj_per_page,
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