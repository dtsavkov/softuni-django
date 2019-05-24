from django.urls import path, re_path, include

from . import views

urlpatterns = [
    path('', views.UnitsList.as_view(), name='units'),
    path('mine/', views.UnitsUserList.as_view(), name='units-mine'),
    path('create/unit/', views.UnitCreate.as_view(), name='unit-create'),
    re_path('^details/(?P<pk>\d+)/$', views.UnitDetails.as_view(), name='unit-details'),
    re_path('^edit/(?P<pk>\d+)/$', views.UnitEdit.as_view(), name='unit-edit'),
    re_path('^delete/(?P<pk>\d+)/$', views.UnitDelete.as_view(), name='unit-delete'),

    path('/unit_types/', views.UnitTypeList.as_view(), name='unit-types'),
    path('create/unit_type/', views.UnitTypeCreate.as_view(), name='unit-type-create'),
    re_path('^edit/unit_type/(?P<pk>\d+)/$', views.UnitTypeEdit.as_view(), name='unit-type-edit'),
    re_path('^delete/unit_type/(?P<pk>\d+)/$', views.UnitTypeDelete.as_view(), name='unit-type-delete'),

]
