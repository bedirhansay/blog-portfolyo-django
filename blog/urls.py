from django.urls import path
from .views import homepage, profile, category, mypost, singlePost, addPost,updatePost,deletePost
from .views import signout, changePassword
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', homepage, name='anasayfa'),
    path('profile/', profile, name='profile'),
    path('posts/',mypost, name='mypost'),
    path('add-post/',addPost, name='add-post'),
    path('logout/',signout, name='signout'),
    path('login/',auth_views.LoginView.as_view(
        template_name='auth/login.html',), name='login'),
    path('change-password/',changePassword, name='change-password'),
    path('update-post/<slug:slug>',updatePost, name='update-post'),
    path('delete-post/<slug:slug>',deletePost, name='delete-post'),
    path('category/<slug:slug>',category, name='category'),
    path('single-post/<slug:slug>',singlePost, name='single-post'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
