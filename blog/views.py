from django.shortcuts import render, get_object_or_404
from .models import BlogObject
# Create your views here.


def all_blogs(request):
    
    blogs = BlogObject.objects.order_by('-date')[:5]
    return render(request, 'blog/all_blogs.html', {'blogs': blogs}) 

def detail(request, blog_id):
    blog = get_object_or_404(BlogObject, pk=blog_id)
    return render(request, 'blog/detail.html',{'blog': blog})