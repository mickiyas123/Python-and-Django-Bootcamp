# import the neccessary module and models
from django import forms
from django.db.models import fields
from blog.models import Post,Comment
from mysite.blog import models



# a class for creating forms for the post based on the models
class PostForm(forms.ModelForm):
     
    # connects the model to the form field
    class meta():
        model = Post
        # connects to the fields neccessary
        fields = ('author','title','text')

# a class for creating forms for the comment based on the models
class CommentForm(forms.ModelForm):

    # connects the model to the form field
    class meta():
        model = Comment
        # connects to the field necessary
        fields = ('author','text')



