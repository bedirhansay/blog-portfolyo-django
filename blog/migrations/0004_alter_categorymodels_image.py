# Generated by Django 4.2.4 on 2023-08-05 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_category_categorymodels'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorymodels',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='blog/static/category_images/'),
        ),
    ]