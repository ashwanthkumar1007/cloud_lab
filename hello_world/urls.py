# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 17:54:45 2020

@author: ashva
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 16:42:03 2020

@author: ashva
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home')
    ]