from django.urls import path
from django.conf.urls import url
from django.urls.conf import re_path
from . import views

urlpatterns = [
    path('',views.register, name='home')
]