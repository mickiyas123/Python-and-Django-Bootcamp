# imported the modules 
from django.urls import path,include
from blog import views


urlpatterns = [
    # route to the home page
    path('/',views.views.PostListViewas_view(),name='post_list'),
    # route to the AboutView
    path('about/',views.Aboutview.as_view(),name = 'about'),
]