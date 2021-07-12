from django.db import models
from django.shortcuts import render
from django.utils import timezone
from django.views.generic import (View,CreateView,TemplateView,
                                  ListView,DeleteView,DetailView)
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
