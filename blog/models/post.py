from django.db import models
from autoslug import AutoSlugField
from .category import CategoryModel
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from .dateAbstract import DateAbstract

class PostModel(DateAbstract):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique=True)
    author = models.ForeignKey(User,related_name='posts', on_delete=models.CASCADE)
    content = RichTextField()
    categories = models.ManyToManyField(CategoryModel, related_name='post')
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return  self.title
    
    class Meta:
        verbose_name= 'Post'
        verbose_name_plural = 'Posts'
        db_table = 'post'
        ordering = ['-publish_date']