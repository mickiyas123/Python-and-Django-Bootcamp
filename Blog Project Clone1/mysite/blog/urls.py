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
    url(r'^post/(?P<pk>\d+)$',views.PostListView.as_view(),name="post_detail"),
    # route to creating a new post
    path('post/new',views.CreatePostView.as_view,name="post_new"),
    # route to edit the post
    url(r'^post/(?P<pk>+d+)/edit/',views.PostUpdateView.as_view(),name='update_post')
    
]