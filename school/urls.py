# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 18:42:36 2020

@author: Mayank Parashar
"""


from django.urls import path
from . import views

urlpatterns = [
    path('',views.post_list,name='post_list'),
    ]