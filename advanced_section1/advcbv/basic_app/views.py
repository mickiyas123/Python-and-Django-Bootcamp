from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView
from django.http import HttpResponse
from . import models

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

class SchoolListView(ListView):
    context_object_name = "schools"
    model = models.School
    # School List

class SchoolDetailView(DetailView):
    context_object_name = "school_detail"
    model = models.School
    template_name = 'basic_app/school_detail.html'        


