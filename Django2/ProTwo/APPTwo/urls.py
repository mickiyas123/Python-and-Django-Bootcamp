from django.conf.urls import url
from APPTwo import views

urlpatterns=[
    # url(r'^$',views.help,name="help"),
    url(r'^$',views.user,name="user"),
]