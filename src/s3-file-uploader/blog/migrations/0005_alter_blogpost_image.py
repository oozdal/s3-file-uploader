# Generated by Django 4.2 on 2023-04-25 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blogpost_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.FileField(default='blog_images/default.png', upload_to='blog_images/'),
        ),
    ]