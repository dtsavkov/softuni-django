from django.urls import path, re_path, include

from . import views

urlpatterns = [
    path('', views.UnitsList.as_view(), name='units'),

]
