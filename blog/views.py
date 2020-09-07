from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from django.views.generic.edit import CreateView, UpdateView

class HomePage(ListView):
    model = Post
    template_name = 'home.html'

class BlogPage(DetailView):
    model = Post
    template_name = 'Detail_Blog.html'

class NewBlog(CreateView):
    model = Post
    template_name = 'new_post.html'
    fields = ['title', 'author', "body"]

class EditBlog(UpdateView):
    model = Post
    template_name = 'EditBlog.html'
    fields = ['title',"body"]


