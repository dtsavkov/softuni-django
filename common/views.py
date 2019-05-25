from django.views import generic
from django.shortcuts import render


def landing(request):
    return render(request, 'landing_page.html')


def about_us(request):
    return render(request, 'about_us.html')


def products(request):
    return render(request, 'products.html')


def services(request):
    return render(request, 'services.html')


def contacts(request):
    return render(request, 'contacts.html')

