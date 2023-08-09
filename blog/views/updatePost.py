
from django.shortcuts import render,redirect, get_object_or_404
from blog.models import PostModel
from blog.forms import UpdatePostForm
from django.contrib.auth.decorators import login_required

@login_required
def updatePost(request,slug):
    
    post = get_object_or_404(PostModel, slug=slug)
    form = UpdatePostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('single-post', slug=post.slug)
   
    return render (request, 'forms/updatePostForm.html', {'form':form} )
