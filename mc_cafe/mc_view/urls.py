from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),


    # REGISTER AND LOGIN #
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),

    # REGISTER AND LOGIN #

    # COFFEE #
    path('mc_coffee/', coffee, name='coffee'),
    path('category_coffee/<int:category_coffee_id>/', get_category_coffee, name='category_coffee'),
    path('coffee/<int:coffee_id>/', view_coffee, name='view_coffee'),
    # COFFEE #

    # DILIKATES #
    path('mc_dilikates/', dilikates, name='dilikates'),
    path('category_dilikates/<int:category_dilikates_id>/', get_category_dilikates, name='category_dilikates'),
    path('dilikates/<int:dilikates_id>/', view_dilikates, name='view_dilikates'),
    # DILIKATES #
]