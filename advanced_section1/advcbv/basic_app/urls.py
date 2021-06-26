from django.urls import path
from django.conf.urls import url
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
  path('',views.SchoolListView.as_view(),name='list'),
  url(r'^(?P<pk>\d+)/$',views.SchoolDetailView.as_view(),name='detail'),
  path('create',views.SchoolCreateView.as_view(),name='create')


]