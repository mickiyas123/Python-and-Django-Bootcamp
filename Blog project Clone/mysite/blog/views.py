from django.forms.forms import Form
from django.shortcuts import render
from blog.forms import PostForm, CommentForm
from django.utils import timezone
from blog.models import Post,Comment
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)

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

# a class for dteails of the post
class PostDetailView(DetailView):
    model = Post   


# a class for creating post but only if you are logged in
class CreatePostView(LoginRequiredMixin,CreateView):
    # url to redirect to if user is nor logged in
    login_url = '/login/'
    redirect_field_name = 'blog/post_deatil.html'

    form_class = PostForm 


    model = Post

# a class for editing posts
class PostUpdateView(LoginRequiredMixin,UpdateView):
    # url to redirect to if user is nor logged in
    login_url = '/login/'
    redirect_field_name = 'blog/post_deatil.html'

    form_class = PostForm
    
    model = Post

# a class for deleting posts
class PostDeleteView(LoginRequiredMixin,DeleteView):
     # url to check if the post is deleted and go back to the homepage.
    success_url = reverse_lazy('post_list')

    form_class = PostForm

    


        



