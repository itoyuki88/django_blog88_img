from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm
from django.views.generic.edit import ModelFormMixin

"""
class PostListView(LoginRequiredMixin, ListView):
    model = Post
    #template_name = 'blog/test.html'
    #context_object_name = 'post'
    ordering = ['-date_posted']
"""

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    success_url = "/home"
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title','content', 'img']
    success_url = "/home"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = "/home"


class MixListView(LoginRequiredMixin, ListView, ModelFormMixin):
    model = Post
    form_class = PostForm
    #fields = ['title', 'content', 'img']
    success_url = '/home'
    template_name = 'blog/home.html'
    #context_object_name  = 'post' #意味ない
    ordering = ['-date_posted']
    #paginate_by = 15

    def get(self, request, *args, **kwargs):
        self.object = None
        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        self.object = None
        self.object_list = self.get_queryset()
        form = self.get_form()
        form.instance.author = self.request.user
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


"""
class ListAndCreateView(PostListView,PostCreateView):
    #object_list=["post"]
   
    def get(self, request, *args, **kwargs):

        listView = PostListView.get(self, request, *args, **kwargs)
        formView = PostCreateView.get(self, request, *args, **kwargs)
        listData = listView.context_data['object_list']
        formData = formView.context_data['form']
        context = {'form' : formData, 'post_list' : listData}
        return render(request, 'blog/test.html', context)
"""