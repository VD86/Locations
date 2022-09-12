from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin
from routes.models import Post
from django.db.models import Q
from .forms import AuthUserForm, RegisterUserForm, CommentForm
from django.contrib.auth.models import User                # для разгоаничения прав-доступа
from django.contrib.auth.mixins import LoginRequiredMixin  # для разгоаничения прав-доступа


class ListObjectsView(ListView):
    model = Post
    template_name = 'main.html'
    context_object_name = 'posts'


class CustomSuccessMessageMixin:
    '''Класс для отображения сообщений'''
    @property
    def success_msg(self):
        return False
    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super().form_valid(form)
    def get_success_url(self):
        return '%s?id=%s' % (self.success_url, self.object.id)


class DetailObjectsView(CustomSuccessMessageMixin, FormMixin, DetailView):
    model = Post
    template_name = 'detail.html'
    context_object_name = 'post'
    form_class = CommentForm
    success_msg = 'Комментарий создан. Отправлен на модерацию'


    def get_success_url(self, **kwargs):
        return reverse_lazy('detail', kwargs={'pk':self.get_object().id})

    def post(self,request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.post = self.get_object()
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class SearchResultsView(ListView):
    '''Класс для поиска'''
    model = Post
    template_name = 'search_results.html'
    context_object_name = 'post'

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Post.objects.filter(Q(image__icontains=query) | Q(title__icontains=query))
        return object_list


class NeedUpdateView(CustomSuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'edit.html'
    fields = 'image','title', 'desc'
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    success_url = '/'
    success_msg = 'Запись обновлена'


class PostDeleteView(LoginRequiredMixin, DeleteView):
    '''Класс для удаления постов'''
    model = Post
    template_name = 'delete.html'
    success_url = '/'
    login_url = '/login/'
    redirect_field_name = 'redirect_to'


class PostCreateView(CustomSuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Post
    fields = ['author','image', 'desc', 'title']
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'create.html'
    success_url = '/'
    success_msg = 'Запись создана'


class ProgectLoginView(AuthUserForm, LoginView):
    form_class = AuthUserForm
    template_name = 'login.html'
    success_url = '/'
    def get_success_url(self):
        '''Переопределение метода get_success_url на success_url'''
        return self.success_url


class RegisterUserView(CustomSuccessMessageMixin, CreateView):
    model = User
    template_name = 'register.html'
    success_url = '/'
    form_class = RegisterUserForm
    success_msg = "Пользователь создан"


class ProgectLogoutView(LogoutView):
    '''Класс выхода'''
    next_page = '/'

class PageObjectsView(ListView):
    '''Класс для второй странички'''
    model = Post
    template_name = 'page.html'
    context_object_name = 'posts'
