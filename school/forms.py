# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 15:40:16 2020

@author: Mayank Parashar
"""


from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)