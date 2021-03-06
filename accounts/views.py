# from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import ProfileUser


def redirect_user(request):
    url = f'/units/'
    return HttpResponseRedirect(url)


class UserDetail(generic.DetailView):
    model = ProfileUser
    template_name = 'user_profile.html'
    context_object_name = 'user'


class Register(generic.CreateView):
    form_class = UserCreationForm
    success_url = '/accounts/login/'
    template_name = 'register.html'

