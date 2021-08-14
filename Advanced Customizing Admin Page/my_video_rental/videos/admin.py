from django.contrib import admin

# Register your models here.
from .models import Movies,Customer

admin.site.register(Movies,Customer)
