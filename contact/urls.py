# contact/urls.py
from django.contrib import admin
#Path is new with Django 2.0 and does not use regex like url
# from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^contact/$', views.contact_view, name='contact'),
]
