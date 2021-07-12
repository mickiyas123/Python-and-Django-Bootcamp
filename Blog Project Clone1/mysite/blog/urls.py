from django import urls
from django.urls import path
from . import views

urlpatterns = [
    # route to the about view
    path('about/',views.AboutView.as_view(),name="about"),
]