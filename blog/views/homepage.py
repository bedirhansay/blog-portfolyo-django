from django.shortcuts import render
from blog.models import PostModel
from django.core.paginator import Paginator

def homepage(request):
    post = PostModel.objects.all().order_by('-publish_date')
    page = request.GET.get('page')
    paginator = Paginator(post, 9)
    return render (request, 'flatpages/Homepage/homepage.html', {'posts': paginator.get_page(page)})
