from django.urls import path
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    path('landing/', views.landing, name='landing'),
    path('about_us/', views.about_us, name='about'),
    path('products/', views.products, name='products'),
    path('services/', views.services, name='services'),
    path('contacts/', views.contacts, name='contacts'),
]