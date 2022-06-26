from django.shortcuts import render
from blog.models import Post
from django.views.generic.edit import DeleteView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views import generic
from django.urls import reverse_lazy
from .models import Post


class PostListView(ListView):

    # specify the model for list view
    model = Post

    # specify the fields to be displayed
    fields = ['__all__']
    template = 'blog/post_list.html'
    
# Create another view, PostCreateView, which inherits django’s generic CreateView, with attributes:

class PostCreateView(CreateView):

    # specify the model for list view
    model = Post

    # specify the fields to be displayed
    fields = ['__all__']

    success_url  = 'reverse_lazy(“blog:all”)'
    template = 'blog/post_form.html'


# Create another view, PostDetailView, which inherits django’s generic DetailView, with attributes:

class PosDetailView(DetailView):
    model = Post

    fields = ['__all__']
    template_name = 'blog/post_detail.html'
    

#Create another view PostUpdateView, which inherits django’s generic UpdateView, with attributes:

class PosUpdateView(UpdateView):
    model = Post

    fields = ['__all__']
    template_name = 'blog/post_form.html'
    success_url  = 'reverse_lazy(“blog:all”)'

#Create another view PostDeleteView, which inherits django’s generic UpdateView, with attributes:

class PosDeleteView(DeleteView):
    model = Post

    fields = ['__all__']
    template_name = 'post_confirm_delete.html'
    success_url  = 'reverse_lazy(“blog:all”)'