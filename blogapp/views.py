from django.shortcuts import render, get_object_or_404
from .models import Blog

def home(request):
    return render(request, 'blog/index.html')
    #blogs=Blog.objects.all
    #return render(request, 'blog/index.html', {'blogs':blogs})

def new(request):
    return render(request, 'blog/contact.html')

def blogs(request):
    blogs=Blog.objects.all
    return render(request, 'blog/blogs.html', {'blogs':blogs})
    #posts = get_object_or_404(Blog, pk=blog_id)
    #eturn render(request, 'blog/details.html', {'posts':posts})

def details(request, blog_id):
    posts = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/details.html', {'posts': posts})

