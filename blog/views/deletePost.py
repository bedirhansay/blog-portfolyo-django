
from django.shortcuts import render,redirect, get_object_or_404
from blog.models import PostModel
from blog.forms import UpdatePostForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def deletePost(request,slug):
    
    post = get_object_or_404(PostModel, slug=slug, author=request.user)
    post.delete()
    return redirect('/profile')
   
    
