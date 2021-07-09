# imported the modules 
from django import urls
from django.urls import path,include
from blog import views
from django.conf.urls import url


urlpatterns = [
    # route to the home page
    path('/',views.views.PostListViewas_view(),name='post_list'),
    # route to the AboutView
    path('about/',views.Aboutview.as_view(),name = 'about'),
    # url for accessing the post detail using regular expression
    url(r'post/(?P<pk>\d+)$',views.PostDetailView.as_view(),name = 'post_detail'),
    # path to create a new post
    path('postnew/',views.CreatePostView.as_view(), name='post_new'),
    # url to edit posts
    url(r'post/(?P<pk>\d+)/edit/$',views.PostUpdateView.as_view(),name='post_edit'),
    # url to delete posts
    url(r'post/(?P<pk>\d+)/remove/$',views.PostDeleteView.as_view(), name='post_remove')

]