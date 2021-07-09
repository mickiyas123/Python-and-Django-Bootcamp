from django.shortcuts import render
from django.utils import timezone
from django.views.generic.list import ListView
from blog.models import Post,Comment
from django.views.generic import (TemplateView,ListView,DetailView)

# Create your views here.

# a templateview for accessing the templates
class Aboutview(TemplateView):
    template_name = 'about.html'

# a class to get list of the posts    
class PostListView(ListView):
    model = Post

    # Python version of sql for post that are greater than the current date and order them by desecending order
    def get_queryset(self):
        # lte means less than or equal to
        return Post.objects.filter(published_date__lte = timezone.now().order_by('-published_date'))




        



