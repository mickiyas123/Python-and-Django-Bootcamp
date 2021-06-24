from django.urls import path
from django.urls.resolvers import URLPattern
from basic_app import views
import basic_app

app_name = 'basic_app'

urlpatterns = [
    path('',views.SchoolListView.as_view(),name=list)
]