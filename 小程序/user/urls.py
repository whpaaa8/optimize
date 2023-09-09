from django.urls import path, include
from .views import user_list, login, register

urlpatterns = [
    path('list/', user_list),
    path('login', login),
    path('register', register),
]
