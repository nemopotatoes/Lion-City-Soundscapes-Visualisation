from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

def about_page(request):
    return render(request, 'about.html')

def map_page(request):
    return render(request, 'map.html')

def contact_page(request):
    return render(request, 'contact.html')
