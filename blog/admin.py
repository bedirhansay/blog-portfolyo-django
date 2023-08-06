from django.contrib import admin
from .models import CategoryModel, PostModel, CommentModel, ContactModel

@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'slug']  # Admin panelinde listede görünecek alanlar


@admin.register(PostModel)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'publish_date', 'update_date', 'image']  
    list_filter = ['publish_date', 'author']  
    search_fields = ['title', 'content']  


@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'user', 'publish_date', 'update_date', 'content']  
    list_filter = ['publish_date', 'user']  
    search_fields = ['content'] 


@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'message', 'publish_date']  
    list_filter = ['publish_date']  
    search_fields = ['name', 'subject']

