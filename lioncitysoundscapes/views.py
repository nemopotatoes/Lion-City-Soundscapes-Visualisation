from django.shortcuts import render
from django.http import HttpResponse

def about_page(request):
    return render(request, 'about.html')

def map_page(request):
    return render(request, 'map.html')