from django.shortcuts import render,get_object_or_404
from blog.models import PostModel,CategoryModel
from django.core.paginator import Paginator


def category(request,slug):
    category = get_object_or_404(CategoryModel, slug=slug)
    post = category.post.all().order_by('-publish_date')
    return render (request, 'flatpages/CategorySinglePage/category.html', {'posts':post,
                                                                            'category':category})
