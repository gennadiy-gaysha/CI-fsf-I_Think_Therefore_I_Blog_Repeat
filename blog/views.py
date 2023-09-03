from django.shortcuts import render
from django.views import generic
from .models import Post

class ListView(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    paginate_by = 6
    template_name = 'index.html'
