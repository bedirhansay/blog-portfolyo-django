from django.shortcuts import render
from django.shortcuts import get_object_or_404
from blog.models import PostModel   
from blog.forms import AddCommentForm

def singlePost(request,slug):
    yazi = get_object_or_404(PostModel,slug=slug)
    post = PostModel.objects.all().order_by('-publish_date')
    form = AddCommentForm()
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = yazi
        comment.user = request.user
        comment.save()
    return render (request, 'flatpages/singlePost/singlePost.html', {'post':yazi, 'posts':post,"form":form})
