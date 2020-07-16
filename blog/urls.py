from django.urls import path
from . import views

'''
Here we're importing Django's function path and all of our views from the blog application. 
(We don't have any yet, but we will get to that in a minute!)
'''

urlpatterns = [
    path('', views.post_list, name='post_list'),
]

#https://tutorial.djangogirls.org/en/django_urls/
#Towards the bottom of the page, I can't write all that