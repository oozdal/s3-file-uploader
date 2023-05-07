# Generated by Django 4.2 on 2023-04-25 22:12

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blogpost_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.FileField(default='blog_images/default.png', upload_to=blog.models.user_directory_path),
        ),
    ]
