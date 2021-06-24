from django.shortcuts import render
from django.http import HttpResponse
from APPTwo.models import User
from . import forms

# Create your views here.

def index(request):
    return render(request,'APPTwo/index.html')

def help(request):
    my_dict={'insert_me':'Help Page'}
    return render(request,'APPTwo/help.html',context=my_dict)

def user(request):

    form =forms.NewUserForm()

    if request.method == "POST":
        form =forms.NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')

    return render(request,'APPTwo/user.html',{'form':form}) 