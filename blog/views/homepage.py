from django.shortcuts import render
from blog.models import PostModel
from django.core.paginator import Paginator
from django.db.models import Q
from blog.forms import ContactForm

def homepage(request):
    query = request.GET.get('filter')
    post = PostModel.objects.all().order_by('-publish_date')
    trends = PostModel.objects.all().order_by('-view_count')[:3]
    contact = ContactForm()

    if request.method == 'POST':
        contact = ContactForm(request.POST)
        if contact.is_valid():
            contact.save()
            contact = ContactForm()

    if query:
        post = post.filter(
            Q(title__icontains=query)|
            Q(categories__name__icontains=query)|
            Q(author__username__icontains=query)|
            Q(content__icontains=query)
        ).distinct()
    page = request.GET.get('page')
    paginator = Paginator(post, 9)
    return render (request, 'flatpages/Homepage/homepage.html', {'posts': paginator.get_page(page),
                                                                  'trends': trends, 'contact': contact})
