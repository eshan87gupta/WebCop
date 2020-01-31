from django.conf.urls import url
from .. import views

urlpatterns = [

        url(r'pollatlon$', views.PoliceLocation.as_view(), name='pollatlon'),
]