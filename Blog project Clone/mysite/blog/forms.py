# import the neccessary module and models
from django import forms
from django.db.models import fields
from django.forms import widgets
from blog.models import Post,Comment
from mysite.blog import models



# a class for creating forms for the post based on the models
class PostForm(forms.ModelForm):
     
    # connects the model to the form field
    class meta():
        model = Post
        # connects to the fields neccessary
        fields = ('author','title','text')
        
        # this will make it connect to the css classes
        widgets ={
            'title':forms.Textarea(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }

# a class for creating forms for the comment based on the models
class CommentForm(forms.ModelForm):

    # connects the model to the form field
    class meta():
        model = Comment
        # connects to the field necessary
        fields = ('author','text')

        # this will make it connect to the css classes
        widgets={
            'author':forms.Textarea(attrs={'class': 'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }



