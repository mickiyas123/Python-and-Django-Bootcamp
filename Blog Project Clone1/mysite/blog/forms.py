# importing modules to be used
from django import forms
from django.db.models import fields
from django.forms import widgets
from blog import models
from blog.models import Post,Comment

# class for forms that are based on the models
class PostForm(forms.ModelForm):
    
    # a class within a class to connect to the model
    class Meta:
        model = Post
        fields = ('author','title','text')

        # widgets to access specific element of the post and apply css classes
        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable  medium-editor-textarea postcontent'})
        }

# class for forms that are based on the models
class CommentForm(forms.ModelForm):

    # a class within a class to connect to the model
    class Meta:
        model = Post
        fields = ('author','text')

        # widgets to access specific elements of the comment and apply css classes
        widgets = {
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }


    
