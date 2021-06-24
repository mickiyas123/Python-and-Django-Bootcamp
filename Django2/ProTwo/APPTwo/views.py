from django.shortcuts import render
from django.http import HttpResponse
from APPTwo.models import User

# Create your views here.

def index(request):
    return render(request,'APPTwo/original_index.html')

def help(request):
    my_dict={'insert_me':'Help Page'}
    return render(request,'APPTwo/help.html',context=my_dict)

def user(request):
    user_list=User.objects.order_by('first_name')
    my_dict={'full_info':user_list}
    return render(request,'APPTwo/index.html',context=my_dict)    