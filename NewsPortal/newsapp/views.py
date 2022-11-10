from datetime import datetime
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm
from .filters import PostFilter

class PostsList(ListView):
    model = Post
    ordering = '-dateCreation'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['number_of_news'] = "Количество новостей:"
        return context


def get_queryset(self):
    queryset = super().get_queryset()
    self.filterset = PostFilter(self.request.GET, queryset)
    return self.filterset.qs


def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    # Добавляем в контекст объект фильтрации.
    context['filterset'] = self.filterset
    return context


class PostDetail(DetailView):
    model = Post
    template_name = 'news_id.html'
    context_object_name = 'news_id'
    pk_url_kwarg = 'id'

class PostCreate(CreateView):
    model = Post
    template_name = 'create.html'
    form_class = PostForm


    # def form_valid(self, form):
    #     news_id = form.save(commit=False)
    #     news_id.categoryType = NEWS
    #     return super().form_valid(form)
    #
    # def form_valid(self, form):
    #     news_id = form.save(commit=False)
    #     news_id.categoryType = ARTICLE
    #     return super().form_valid(form)


class PostUpdate(UpdateView):
    model = Post
    template_name = 'create.html'
    form_class = PostForm



class PostDelete(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('post_list')




class PostSearch(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'posts'
    ordering = ['-dateCreation']
    paginate_by = 3
    success_url = reverse_lazy('post_list')


    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context



