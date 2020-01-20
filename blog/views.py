from django.shortcuts import render, get_object_or_404
from .models import Blog


# Create your views here.
def blogs(request):
    blogs = Blog.objects
    return render(request, 'blog/blogs.html', {'blogs': blogs})


def details(request, blog_id):
    detailblog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/details.html', {'blog': detailblog})
