# contact/urls.py
from django.contrib import admin
#Path is new with Django 2.0 and does not use regex like url
# from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    # path('contact/', views.ContactView, name='contact'),
    # path('success/', views.successView, name='success'),
    url(r'contact/', views.contactView, name='contact'),
    url(r'success/', views.successView, name='success'),
]
