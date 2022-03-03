from django.shortcuts import get_object_or_404, redirect, render

from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth import login, logout

# Create your views here.

def base(request):
    return render(request, 'base.html')


def home(request):
    return render(request, 'mc_window/home.html')




# REGISTER AND LOGIN AND LOGOUT #

def register(request):
    if request.method == 'POST':
       form = UserRegisterForm(request.POST, request.FILES)
       if form.is_valid():
           user = form.save()
           login(request, user)
           messages.success(request, 'Вы успешно зарегистрировались!')
           return redirect('/')
       else:
            messages.error(request, 'Ошибка при регистраций!')
    else:
        form = UserRegisterForm()
    return render(request, 'mc_window/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Ошибка при входе!')
    else:
        form = UserLoginForm()
    return render(request, 'mc_window/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('/')

# REGISTER AND LOGIN AND LOGOUT #


# COFFEE #


def coffee(request):
    coffee = MC_Coffee.objects.all()
    categories_coffee = Category_Coffee.objects.all()
    return render(request, 'mc_menu/coffee.html', {'coffee': coffee, 'category_coffee': categories_coffee})

def get_category_coffee(request, category_coffee_id):
    coffee = MC_Coffee.objects.filter(category_coffee_id=category_coffee_id)
    categories_coffee = Category_Coffee.objects.all()
    category_coffee = Category_Coffee.objects.get(pk=category_coffee_id)
    return render(request, 'mc_menu/category_coffee.html', {'coffee': coffee, 'categories_coffee': categories_coffee, 'category_coffee': category_coffee})

def view_coffee(request, coffee_id):
    # coffee_item = MC_Coffee.objects.get(pk=coffee_id)
    coffee_item = get_object_or_404(MC_Coffee, pk=coffee_id)
    return render(request, 'mc_menu/view_coffee.html', {'coffee_item': coffee_item})

# COFFEE #

# DILIKATES

def dilikates(request):
    dilikates = MC_Dilikates.objects.all()
    categories_dilikates = Category_Dilikates.objects.all()
    return render(request, 'mc_menu/dilikates.html', {'dilikates': dilikates, 'category_dilikates': categories_dilikates})

def get_category_dilikates(request, category_dilikates_id):
    dilikates = MC_Dilikates.objects.filter(category_dilikates_id=category_dilikates_id)
    categories_dilikates = Category_Dilikates.objects.all()
    category_dilikates = Category_Dilikates.objects.get(pk=category_dilikates_id)
    return render(request, 'mc_menu/category_dilikates.html', {'dilikates': dilikates, 'categories_dilikates': categories_dilikates, 'category_dilikates': category_dilikates})


def view_dilikates(request, dilikates_id):
    # dilikates_item = MC_Dilikates.objects.get(pk=dilikates_id)
    dilikates_item = get_object_or_404(MC_Dilikates, pk=dilikates_id)
    return render(request, 'mc_menu/view_dilikates.html', {'dilikates_item': dilikates_item})

# DILIKATES
