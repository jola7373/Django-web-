from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
"""ListView-->allow query set in the database"""
"""detailView--> details of one blog post"""
# Create your views here.

#def home(request):
    #return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_detail.html'