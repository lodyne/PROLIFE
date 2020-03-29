from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='blog-home'),
    path('about/',views.about,name='blog-about'),
    path('sala/',views.sala,name='blog-sala'),
    path('post/',views.post,name='blog-post'),
    path('contact/',views.contact,name='blog-contact')
    
]
