from django.contrib import admin
from .models import BlogPost
#from .models import Comment
from .models import Category

admin.site.register(BlogPost)

#class AuthorAdmin(admin.ModelAdmin):
#    list_display = ('title', 'id', 'status', 'slug', 'author')
#    prepopulated_fields = {'slug': ('title',), }
    
#admin.site.register(Comments)

#class CommentAdmin(admin.ModelAdmin):
#    list_display = ('post', 'name', 'email',  'publish', 'status')
#    list_filter = ('status', 'publish')
#    search_fields = ('name', 'email', 'content')

admin.site.register(Category)
