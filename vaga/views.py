# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    
    return render(request, 'vaga/index.html')
    
def quickWeigh(request):
    return render(request, 'vaga/quickWeigh.html')
    
def detailWeigh(request):
    return render(request, 'vaga/detailWeigh.html')
