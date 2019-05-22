from django.shortcuts import render
from django.views import generic

from .models import Units


class UnitsList(generic.ListView):
    model = Units                           # return all units
    template_name = 'units_list.html'
    context_object_name = 'units'

