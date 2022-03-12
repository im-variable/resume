from django.urls import path
from . views import home_page, about, resume, projects, contact
from django.views.generic.base import RedirectView
from django.conf.urls import url

urlpatterns = [
    # path('', home_page, name='home'),

    path('a/', about, name='about'),
    path('r/', resume, name='resume'),
    path('p/', projects, name='projects'),
    path('c/', contact, name='contact'), 

    path('<str:uname>', home_page, name='home'),
    path('a/<str:uname>', about, name='about'),
    path('r/<str:uname>', resume, name='resume'),
    path('p/<str:uname>', projects, name='projects'),
    path('c/<str:uname>', contact, name='contact'), 
]
