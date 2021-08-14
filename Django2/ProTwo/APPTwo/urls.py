from django.conf.urls import include, url
from APPTwo import views
from django.conf import settings    

urlpatterns=[
    # url(r'^$',views.help,name="help"),
    url(r'^$',views.user,name="user"),
]

# checking to see Debug is true
if settings.DEBUG:
    import debug_toolbar
    # creating debug toolbar and conactinating with other urls
    urlpatterns = [
        url(r'^__debug__/',include(debug_toolbar.urls))
    ] + urlpatterns