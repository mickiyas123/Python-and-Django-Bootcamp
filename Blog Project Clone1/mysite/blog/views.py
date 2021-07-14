from django.db import models
from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from blog.forms import CommentForm, PostForm
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

##################################################################
##################################################################'

# a function to publish draft posts
@login_required
def post_publish(request,pk):
    post =get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('post_detail',pk=pk)


# a function view to comment on posts
@login_required
def add_comments_to_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        form  = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail.html',pk=post.pk)
    else:
        form = CommentForm()
    return render(request,'blog/comment_form.html',{'form':form})   


# a function based view for comment approval
@login_required
def comment_approve(request,pk):
    # to get the comment 
    comment = get_object_or_404(Comment,pk=pk)
    # calling the approve method in models.py
    comment.approve()
    # redirecting to the post detail page
    return redirect('post_detail.html',pk=comment.post.pk)

# a function based view for deleting comments
@login_required
def remove_comment(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail',pk=post_pk)

