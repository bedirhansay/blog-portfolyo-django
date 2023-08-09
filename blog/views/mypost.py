from django.shortcuts import render
from blog.models import PostModel,CategoryModel

def mypost(request):
    posts = PostModel.objects.filter(author=request.user)
    return render (request, 'flatpages/mypost/mypost.html', {'posts':posts})
