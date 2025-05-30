from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def home(request):
    return render(request,'blog/home.html')


def post_list(request):
    posts = Post.objects.filter(is_published=True).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})