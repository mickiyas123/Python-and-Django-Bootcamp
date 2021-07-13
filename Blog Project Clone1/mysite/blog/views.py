from django.db import models
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from blog.forms import PostForm
from django.urls import reverse_lazy
from django.views.generic import (View,CreateView,TemplateView,
                                  ListView,DeleteView,DetailView,UpdateView)
from blog.models import Post,Comment


# Create your views here.

# template view class to access a template
class AboutView(TemplateView):
    template_name = 'about.html'

# A home Page for the web which is the list of the posts
class PostListView(ListView):
    model = Post
    
    # a query to get the latest posts
    def get_queryset(self):
        return Post.objects.filter(publish_date__lte = timezone.now()).order_by('-publish_date')

#  a class for detail page of the post
class PostDetailView(DetailView):
    model = Post  

# a class for Creating posts
class CreatePostView(LoginRequiredMixin,CreateView):
    # take them to login page
    login_url  = '/login/'
    # redirect to the detail view
    redirect_field_name = 'blog/post_detail.html'

    form_class = PostForm
    model = Post 


# a class for updating a post
class  PostUpdateView(LoginRequiredMixin, UpdateView):
    # take them to login page
    login_url  = '/login/'
    # redirect to the detail view
    redirect_field_name = 'blog/post_detail.html'
    form_class  = PostForm
    model = Post

# a class for deleting a post  
class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    # after deleting a post it will go to list of the post
    success_url = reverse_lazy('post_list')

# a class to see the unpublished posts
class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'
    model = Post

    # a method to return list of the post with specific value
    def get_queryset(self):
        return Post.objects.filter(publish_date_isnull = True).order_by('created_day')