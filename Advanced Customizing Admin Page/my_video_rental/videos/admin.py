from django.contrib import admin
from . import models
# Register your models here.

# class for order in our model
class MovieAdmin(admin.ModelAdmin):

    fields = ['release_year','title','length']

admin.site.register(models.Customer)
admin.site.register(models.Movies,MovieAdmin)