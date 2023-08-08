from django.urls import path
from .views import homepage, profile, category, mypost
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', homepage, name='anasayfa'),
    path('profile/', profile, name='profile'),
    path('posts/',mypost, name='mypost'),
    path('category/<slug:slug>',category, name='category'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
