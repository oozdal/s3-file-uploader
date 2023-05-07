from django.shortcuts import render
from .models import BlogPost, Category
from django.views.generic import ListView

def home(request):
    return render(request, 'index.html', {'posts': BlogPost.objects.all()})

class CatListView(ListView):
    template_name = 'category.html'
    context_object_name = 'catlist'

    def get_queryset(self):
        content = {
            'cat' : self.kwargs['category'],
            'posts' : BlogPost.objects.filter(category__name=self.kwargs['category'])
            }
        return content

def category_list(request):
    category_list = Category.objects.exclude(name='default')
    context = {
        "category_list" : category_list,
    }
    return context

