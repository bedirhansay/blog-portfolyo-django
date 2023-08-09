
from django.shortcuts import render
from blog.models import PostModel
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def profile(request):
    user = request.user
    post = PostModel.objects.filter(author=user).order_by('-publish_date')
    return render (request, 'flatpages/profile/profile.html', {'posts':post})
