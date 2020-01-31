from django.conf.urls import url
from . import views

urlpatterns = [

    #url(r'^shortestroute/(?P<parameter>[\w-]+)$', views.refreshHtml, name='shortroute'),
    #url(r'^firstshortestroute/(?P<phone_number_vict>[\w-]+)/(?P<phone_number_pol>[\w-]+)$', views.loadHtml, name='shortroute'),
    url(r'^firstshortestroute/(?P<phone_number_vict>\w+)/(?P<phone_number_pol>\w+)$', views.loadHtml, name='shortroute'),
    url(r'rastaloder$', views.rastaloder, name='rastaloder')

]