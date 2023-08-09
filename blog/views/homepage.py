from django.shortcuts import render
from blog.models import PostModel
from django.core.paginator import Paginator
from django.db.models import Q

def homepage(request):
    filter = request.GET.get('filter')
    post = PostModel.objects.all().order_by('-publish_date')
    trends = PostModel.objects.all().order_by('-view_count')[:3]
    if filter:
        post = post.filter(
            Q(title__icontains=filter)|
            Q(categories__name__icontains=filter)|
            Q(author__username__icontains=filter)|
            Q(content__icontains=filter)
        ).distinct()
    page = request.GET.get('page')
    paginator = Paginator(post, 9)
    return render (request, 'flatpages/Homepage/homepage.html', {'posts': paginator.get_page(page),
                                                                  'trends': trends,})
