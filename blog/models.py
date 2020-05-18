from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    '''Модель категорий'''
    name = models.CharField('Имя', max_length=100)
    slug = models.SlugField('url', max_length=100, unique=True)
    description = models.TextField('Описание', max_length=1000, default='', blank=True)
    parent = TreeForeignKey(
        'self',
        verbose_name='Родительская категория',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )
    template = models.CharField('Шаблон', max_length=500, default='blog/post_list.html')
    published = models.BooleanField('Отображать?', default=True)
    paginated = models.PositiveIntegerField('Количество новостей на странице', default=5)
    sort = models.PositiveIntegerField('Порядок', default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Tag(models.Model):
    '''Модель тегов'''
    name = models.CharField('Имя', max_length=100)
    slug = models.SlugField('url', max_length=100, unique=True)
    published = models.BooleanField('Отображать?', default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Post(models.Model):
    '''Модель постов'''
    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    title = models.CharField('Заголовок', max_length=100)
    mini_text = models.TextField("Короткий тест", max_length=100)
    subtitle = models.CharField('Под заголовок', max_length=500, blank=True, null=True)
    text = models.TextField('Основной тест', max_length=5000)
    created_date = models.DateTimeField('Дата создания', auto_now_add=True)
    slug = models.SlugField('url', max_length=100, unique=True)
    category = models.ForeignKey(
        Category,
        verbose_name="Категория",
        on_delete=models.CASCADE,
        null=True
    )
    tags = models.ManyToManyField(Tag, verbose_name="Тег", blank=True, related_name='tag')
    edit_date = models.DateTimeField(
        'Дата редактирования',
        default=timezone.now,
        blank=True,
        null=True
    )
    published_date = models.DateTimeField(
        'Дата побликации',
        default=timezone.now,
        blank=True,
        null=True,
    )
    image = models.ImageField('Главная фотография', upload_to='post/', null=True, blank=True)
    template = models.CharField('Шаблон', max_length=500, default='blog/post_detail.html')
    published = models.BooleanField('Опубликовать?', default=True)
    viewed = models.PositiveIntegerField("Просмотрено", default=0)
    status = models.BooleanField("Для зарегистрированных", default=False)
    sort = models.PositiveIntegerField('Порядок', default=0)

    def get_tags(self):
        return self.tags.all()

    def get_absolute_url(self):
        return reverse('detail_post', kwargs={'category': self.category.slug, 'slug': self.slug})

    def get_comments_count(self):
        return self.comments.count()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Comment(models.Model):
    '''Модель комментариев'''
    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE,
    )
    post = models.ForeignKey(Post,
                             verbose_name="Статья",
                             on_delete=models.CASCADE,
                             related_name='comments'
                             )
    text = models.TextField('Тест', max_length=500)
    created_date = models.DateTimeField('Дата создания', auto_now=True)
    moderation = models.BooleanField('Модерация', default=False)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
