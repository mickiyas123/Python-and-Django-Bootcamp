from django.urls import path
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
  path('',views.SchoolListView.as_view(),name='list'),
  path('(?P<pk>[-\w]+)/',views.SchoolDetailView.as_view(),name='detail')


]