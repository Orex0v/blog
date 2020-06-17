from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.
from django.conf import settings


class Menu(models.Model):
    """Меню"""
    name = models.CharField("Имя", max_length=100)
    status = models.BooleanField("Для зарегистрированных?", default=False)
    published = models.BooleanField("Активно?", default=True)
    
    def __str__(self):
        return  self.name

    def items(self):
        return self.menuitem_set.all()
    
    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Менюшки'


class MenuItem(MPTTModel):
    title = models.CharField("Название пункта меню на сайте", max_length=255)
    name = models.CharField("Название латиницей", max_length=255)
    parent = TreeForeignKey(
        'self',
        verbose_name='Родительское пункт',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )
    menu = models.ForeignKey(
        Menu,
        verbose_name="Меню",
        on_delete=models.CASCADE,
    )
    status = models.BooleanField('Только для зарегистрированных', default=False)
    url = models.CharField('url на внешний ресурс', max_length=255, null=True, blank=True)
    anchor = models.CharField("Якорь", max_length=255, null=True, blank=True)
    
    content_type = models.ForeignKey(
        ContentType,
        verbose_name='Ссылка на',
        # limit_choices_to=settings.MENU_APPS,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    object_id = models.PositiveIntegerField(verbose_name='ID записи', default=1, null=True)
    content_object = GenericForeignKey('content_type', 'object_id')
    sort = models.PositiveIntegerField('Порядок', default=0)
    published = models.BooleanField('Отображать?', default=True)
    
    
    def get_ancor(self):
        if self.anchor:
            return "{}/{}".format(Site.objects.get_current().domain, self.anchor)
        else:
            return False
    

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'

