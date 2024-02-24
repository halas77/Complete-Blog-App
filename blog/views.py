from django.shortcuts import render
from .models import Post
from django.views import generic
from django.views.decorators.http import require_GET
from django.http import HttpResponse
# Create your views here.



class PostList(generic.ListView):
    queryset = Post.objects.all().order_by('-created_on')
    print(queryset)
    template_name = 'home.html'
    
    
    
class PostDetail(generic.DetailView):
    model = Post
    template_name = 'detail.html'
    

