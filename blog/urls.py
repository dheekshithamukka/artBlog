from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('blog', views.blogArt, name='blogHome'),
    # API to post a comment
    path('postComment', views.postComment, name="postComment"),
    path('', views.blogArt, name='blogHome'),
    path('<str:slug>', views.blogPost, name='blogPost'),

]
