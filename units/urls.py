from django.urls import path, re_path, include

from . import views

urlpatterns = [
    path('', views.UnitsList.as_view(), name='units'),
    path('mine/', views.UnitsUserList.as_view(), name='units-mine'),
    path('create/', views.UnitCreate.as_view(), name='unit-create'),
    re_path('^details/(?P<pk>\d+)/$', views.UnitDetails.as_view(), name='unit-details'),
    re_path('^delete/(?P<pk>\d+)/$', views.UnitDelete.as_view(), name='unit-delete'),
    # re_path('^edit/(?P<pk>\d+)/$', views.UnitEdit.as_view(), name='unit-edit'),

]
