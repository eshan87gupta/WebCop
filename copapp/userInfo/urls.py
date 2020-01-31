from django.conf.urls import url
from .. import views

urlpatterns = [

        url(r'userinfo$', views.UserInfoList.as_view(), name='userinfo'),
]