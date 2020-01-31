from django.conf.urls import url
from .. import views

urlpatterns = [

        url(r'viclatlon$', views.VictimLocation.as_view(), name='viclatlon'),
]