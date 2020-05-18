from datetime import datetime

from django.shortcuts import render
from django.views.generic.base import View

from .models import Category, Post, Tag


class HomeView(View):
    '''Главная страница'''
    def get(self, request):
        category_list = Category.objects.all()
        post_list = Post.objects.filter(published_date__lte=datetime.now(), published=True)
        tag_list = Tag.objects.filter(published=True)
        return render(request, 'blog/post_list.html', {'categories': category_list,
                                                       'post_list': post_list,
                                                       'tags': tag_list
                                                       })


class PostDetailView(View):
    '''Вывод полной статьи'''
    def get(self, request, category, slug):
        category_list = Category.objects.all()
        post = Post.objects.get(slug=slug)
        return render(request, post.template, {'categories': category_list, 'post': post})


class CategoryView(View):
    '''Вывод статей категории'''
    def get(self, request, category_name):
        category = Category.objects.get(slug=category_name)
        post_list = Post.objects.filter(category_id=category.id,
                                        published_date__lte=datetime.now(),
                                        published=True
                                        )
        return render(request, category.template, {'category': category, 'post_list': post_list})


class TagView(View):
    '''Вывод статей по тегу'''
    def get(self, request, slug):
        tag = Tag.objects.get(slug=slug)
        post_list = Post.objects.filter(tags=tag.id, published_date__lte=datetime.now(), published=True)
        return render(request, 'blog/tag_list.html', {'post_list': post_list})
