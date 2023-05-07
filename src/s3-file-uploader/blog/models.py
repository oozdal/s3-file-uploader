from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

def user_directory_path(instance, filename):
    return 'blog_images/{0}/{1}'.format(instance.category, filename)

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class BlogPost(models.Model):

    #class NewManager(models.Manager):
    #    def get_queryset(self):
    #        return super().get_queryset() .filter(status='published')

    #options = (
    #    ('draft', 'Draft'),
    #    ('published', 'Published'),
    #)

    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    body = models.TextField()
    image = models.FileField(upload_to=user_directory_path, default='blog_images/default.png')

    #publish = models.DateTimeField(default=timezone.now)
    #author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    #content = models.TextField()
    #status = models.CharField(max_length=10, choices=options, default='draft')
    #objects = models.Manager()  # default manager
    #newmanager = NewManager()  # custom manager

    #def get_absolute_url(self):
    #    return reverse('blog:post_single', args=[self.slug])

    #class Meta:
    #    ordering = ('-publish',)

    def __str__(self):
        return self.title


class Comment(models.Model):

    post = models.ForeignKey(BlogPost,
                             on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=50)
    email = models.EmailField()
    content = models.TextField()
    publish = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ('publish',)

    def __str__(self):
        return f'Comment by {self.name}'

