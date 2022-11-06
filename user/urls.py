from django.urls import path
from .views import *

urlpatterns = [
    path('register/', userRegister, name='register'),
    path('login/', userLogin, name='login'),
    path('profiles/', profiles, name='profiles'),
    path('olustur/', olustur, name='olustur'),
    path('hesap/', hesap, name='hesap'),
    path('delete/', userDelete, name='delete'),
    path('logout/', userLogout, name='logout')
]