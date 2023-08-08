from django.urls import path
from .views import homepage, profile, category, mypost, singlePost
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', homepage, name='anasayfa'),
    path('profile/', profile, name='profile'),
    path('posts/',mypost, name='mypost'),
    path('category/<slug:slug>',category, name='category'),
    path('single-post/<slug:slug>',singlePost, name='single-post'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
