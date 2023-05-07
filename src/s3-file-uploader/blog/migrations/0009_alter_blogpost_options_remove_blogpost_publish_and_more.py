# Generated by Django 4.2 on 2023-04-25 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_blogpost_options_blogpost_publish_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={},
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='publish',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='status',
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='body',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.FileField(default='blog_images/default.png', upload_to='blog_images/'),
        ),
    ]
