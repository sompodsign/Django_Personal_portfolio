from django.shortcuts import render, get_object_or_404
from .models import Post


def all_blogs(request):
    posts = Post.objects.order_by('-post_date')
    return render(request, 'blog/all_blogs.html', {'posts': posts})

def detail(request, blog_id):
    post = get_object_or_404(Post, pk=blog_id)
    return render(request, 'blog/detail.html', {'post': post})