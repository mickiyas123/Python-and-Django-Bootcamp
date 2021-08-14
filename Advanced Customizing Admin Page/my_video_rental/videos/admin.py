from django.contrib import admin
from . import models
# Register your models here.

# class for manuplating our models
class MovieAdmin(admin.ModelAdmin):
   
    # order  
    fields = ['release_date','title','length','director']
    # search
    search_fields = ['title','length']
    # list filter
    list_filter = ['release_date','length']

    list_display = ['release_date','title','length','director']

admin.site.register(models.Customer)
admin.site.register(models.Movies,MovieAdmin)