from .models import Blog
from django.shortcuts import render, get_object_or_404

def blog(request):
    blog = Blog.objects
    return render(request, 'blog/blog.html', {'blog': blog})


def detail(request, blog_id):
    detailblog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': detailblog})

