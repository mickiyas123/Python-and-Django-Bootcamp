from django.shortcuts import render
from blog.models import Post,Comment
from django.views.generic import (TemplateView)

# Create your views here.

# a templateview for accessing the templates
class Aboutview(TemplateView):
    template_name = 'about.html'



