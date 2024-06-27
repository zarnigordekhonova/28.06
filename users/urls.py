from django.urls import path
from .views import create_user, logout, login


urlpatterns = [
    path('create_user/', create_user, name='create_user'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
]