from django.urls import path
from .views import login

app_name = 'users'

urlpatterns = [
    path('l/', login, name='login'),
]
