from django.contrib import admin
from django.contrib.admin.decorators import register

from .models import School,Student

# Register your models here.

admin.site,register(School)
admin.site.register(Student)
