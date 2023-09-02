from django.shortcuts import render
from django.views.generic.base import View
from .models import Post


class PostView(View): # Будет наследоваться от родительского класса View- где есть уже вся механика
    '''вывод записей'''

    def get(self, request):  # request - информация принитая от user
        posts = Post.objects.all()  # будет ссылаться на всю нашу информацию из таблицы БД

        return render(request, 'blog.html', {'post_list': posts})  # функция render - обьединяет указанный шаблон со словарём


class PostDetail(View):
    '''новая страница записи'''
    def get(self, request, pk):
        posts = Post.objects.get(id=pk)
        return render(request, 'blog_detail.html', {'post': posts})