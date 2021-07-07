# imported the modules 
from django.urls import path,include
from blog import views


urlpatterns = [
    path('about/',views.Aboutview.as_view(),name = 'about'),
]