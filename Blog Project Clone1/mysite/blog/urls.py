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
    url(r'^post/(?P<pk>\d+)/edit/',views.PostUpdateView.as_view(),name='post_edit'),
    # route to delete a post
    url(r'^post/(?P<pk>\d+)/remove/',views.PostDeleteView.as_view,name = 'post_remove'),
    # route to see the unpublished posts
    path('drafts/',views.DraftListView.as_view(),name = 'post_draft_lift'),
    # route to see the comments on the post
    url(r'^post/(?P<pk>\d+)/comment',views.add_comments_to_post,name="add_comment_to_post"),
    # route to approve comments
    url('comment/(?P<pk>\d+)/approve/',views.comment_approve,name="comment_approve"),
    # route to delete comments
    url('comment/(?P<pk>\d+)/approve/',views.remove_comment,name='remove_comment')
    
]