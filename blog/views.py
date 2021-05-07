from django.shortcuts import render,get_object_or_404
from .models import Blog
# Create your views here.

def allblogs(request):

    blogs=Blog.objects.all()

    return render(request,'blog/allblogs.html',{'blogs':blogs})

# finding object by ID of the blog
# this function either returns everything of the object with that ID or returns 404 error if not found in database
def detail(request, blog_id):
    detailblog = get_object_or_404(Blog,pk=blog_id)
    return render(request,'blog/detail.html',{'blog':detailblog})