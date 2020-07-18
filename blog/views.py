from django.shortcuts import render
from .models import Post
from django.utils import timezone


# Create your views here.
def post_list(request): #request is everything we receive from the user via the Internet
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

'''
s you can see, we created a function (def) 
called post_list that takes request and will 
return the value it gets from calling another 
function render that will render (put together) 
our template blog/post_list.html.
'''
