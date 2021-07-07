# import the neccessary module and models
from django import forms
from django.db.models import fields
from blog.models import Post,Comment



# a class for creating forms based on the models
class PostForm(forms.ModelForm):
     
    # connects the model to the form fiekd
    class meta():
        model = Post
        # connects to the fields neccessary
        fields = ('author','title','text')
        


