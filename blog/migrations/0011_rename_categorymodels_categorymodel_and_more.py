# Generated by Django 4.2.4 on 2023-08-05 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_accountmodel'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='categoryModels',
            new_name='CategoryModel',
        ),
        migrations.RenameModel(
            old_name='CommentModels',
            new_name='CommentModel',
        ),
        migrations.RenameModel(
            old_name='ContactModels',
            new_name='ContactModel',
        ),
        migrations.RenameModel(
            old_name='PostModels',
            new_name='PostModel',
        ),
    ]
