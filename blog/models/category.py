from django.db import models
from autoslug import AutoSlugField

class CategoryModel(models.Model):
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='name', unique=True)
    image = models.ImageField(upload_to='blog/media/category_images/', blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name= 'Category'
        verbose_name_plural = 'Categories'
        db_table = 'category'
