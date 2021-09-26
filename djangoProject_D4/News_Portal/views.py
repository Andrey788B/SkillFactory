from django.views.generic import ListView, DetailView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.models import User, Group
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator

from .models import News, Category, BaseRegisterForm
from datetime import datetime
from .filters import NewsFilter
from .forms import NewsForm

class AllNewsList(ListView):
    model = News
    template_name = 'flatpages/news.html'
    context_object_name = 'news'
    queryset = News.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['value1'] = None
        return context


class NewsDetail(DetailView):
    model = News
    template_name = 'flatpages/ArNews.html'
    context_object_name = 'ArNews'


class Filters(ListView):
    model = News
    template_name = 'flatpages/search.html'
    context_object_name = 'search'
    ordering = ['-time']
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset())
        return context


class AdNews(ListView):
    model = News
    template_name = 'flatpages/adnews.html'
    context_object_name = 'adnews'
    queryset = News.objects.order_by('-id')
    paginate_by = 1
    form_class = NewsForm  # добавляем форм класс, чтобы получать доступ к форме через метод POST

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset())

        context['categories'] = Category.objects.all()
        context['form'] = NewsForm()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)  # создаём новую форму, забиваем в неё данные из POST-запроса

        if form.is_valid():  # если пользователь ввёл всё правильно и нигде не ошибся, то сохраняем новый товар
            form.save()

        return super().get(request, *args, **kwargs)


class NewsUpdate(UpdateView):
    template_name = 'flatpages/news_update.html'
    form_class = NewsForm

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте, который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return News.objects.get(pk=id)


# дженерик для удаления товара
class NewsDelete(DeleteView):
    template_name = 'flatpages/news_delete.html'
    queryset = News.objects.all()
    success_url = '/news/'


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'flatpages/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_authors'] = not self.request.user.groups.filter(name='authors').exists()
        return context

class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/news/'


@login_required
def Upgrade_me(request):
    user = request.user
    premium_group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        premium_group.user_set.add(user)
    return redirect('/')


class MyView(PermissionRequiredMixin, IndexView):
    permission_required = ('News_Portal.view_news',
                           'News_Portal.add_news',
                           'News_Portal.delete_news',
                           'News_Portal.change_news')


