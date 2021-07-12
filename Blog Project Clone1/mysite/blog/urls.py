from django import urls
from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    # route to the home page
    path('',views.PostListView.as_view(),name="post_list"),
    # route to the about view
    path('about/',views.AboutView.as_view(),name="about"),
    # route to detail of the posts
    url(r'^post/(?P<pk>\d+)$',views.PostListView.as_view(),name="post_detail")
    
]