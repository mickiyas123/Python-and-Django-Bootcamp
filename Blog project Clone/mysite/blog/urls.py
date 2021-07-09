# imported the modules 
from django.urls import path,include
from blog import views
from django.conf.urls import url


urlpatterns = [
    # route to the home page
    path('/',views.views.PostListViewas_view(),name='post_list'),
    # route to the AboutView
    path('about/',views.Aboutview.as_view(),name = 'about'),
    # url for accessing the post detail using regular expression
    url(r'post/(?P<pk>\d+)$',views.PostDetailView.as_view(),name = 'post_detail')
]