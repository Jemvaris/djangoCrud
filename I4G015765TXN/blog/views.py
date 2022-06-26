
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views import generic
from django.urls import reverse_lazy
from .models import Post


class PostListView(ListView):

    # specify the model for list view
    model = Post
    
# Create another view, PostCreateView, which inherits django’s generic CreateView, with attributes:

class PostCreateView(CreateView):

    # specify the model for list view
    model = Post

    # specify the fields to be displayed
    fields = '__all__'

    success_url  = reverse_lazy('blog:all')
    


# Create another view, PostDetailView, which inherits django’s generic DetailView, with attributes:

class PostDetailView(DetailView):
    model = Post
    

#Create another view PostUpdateView, which inherits django’s generic UpdateView, with attributes:

class PostUpdateView(UpdateView):
    model = Post

    fields = '__all__'
    
    success_url  = reverse_lazy('blog:all')

#Create another view PostDeleteView, which inherits django’s generic UpdateView, with attributes:

class PostDeleteView(DeleteView):
    model = Post

    fields = '__all__'
    success_url  = reverse_lazy('blog:all')