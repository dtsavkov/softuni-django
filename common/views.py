from django.views import generic
from django.shortcuts import render


def landing(request):
    return render(request, 'landing_page.html')


# class Landing(generic.CreateView):
#     template_name = 'landing_page.html'
#     success_url = '/'
