from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin

class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','content']
    success_url = "/home"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title','content']
    success_url = "/home"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = "/home"

