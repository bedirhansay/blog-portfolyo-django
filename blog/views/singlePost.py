from django.shortcuts import render
from django.shortcuts import get_object_or_404
from blog.models import PostModel   

def singlePost(request,slug):
    yazi = get_object_or_404(PostModel,slug=slug)
    post = PostModel.objects.all().order_by('-publish_date')
  
    return render (request, 'flatpages/singlePost/singlePost.html', {'post':yazi, 'posts':post})
