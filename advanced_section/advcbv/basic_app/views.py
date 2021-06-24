from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse


# Create your views here.

class CBview(View):
    def get(self,request):
        return HttpResponse("CLASS BASE VIEWS ARE COOL!")
        
