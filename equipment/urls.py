from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^f/$', views.index, name='index'),
    url(r'^test/$', views.test_form, name='test_form'),
    url(r'^equipment/$', views.EquipmentList.as_view(), name='equipment-list'),
    url(r'^equipment/add/$', views.EquipmentCreate.as_view(), name='equipment-create'),
    url(r'^equipment/(?P<pk>[0-9]+)/$', views.EquipmentDetail.as_view(), name='equipment-detail'),
    url(r'^equipment/(?P<pk>[0-9]+)/update$', views.EquipmentUpdate.as_view(), name='equipment-update'),
    url(r'^equipment/(?P<pk>[0-9]+)/delete/$', views.EquipmentDelete.as_view(), name='equipment-delete'),
]