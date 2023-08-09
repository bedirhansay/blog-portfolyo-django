
from django.shortcuts import render,redirect
from blog.models import PostModel
from blog.forms import AddPostForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def addPost(request):
    form = AddPostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        form.save_m2m()
        messages.success(request, 'Post added successfully')
        return redirect('single-post', post.slug)
    else:
        print(form.errors)
    
   
    return render (request, 'forms/addPostForm.html' , {'form': form})
