# Generated by Django 4.2.4 on 2023-08-05 12:01

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_postmodels_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodels',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
