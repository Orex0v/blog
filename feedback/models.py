from django.db import models
from django.urls import reverse

# Create your models here.
class Feedback(models.Model):
    """Модель обратной связи"""
    email = models.EmailField('Почта', null=False)
    text = models.TextField('Текст', max_length=500)
    
    class Meta:
        verbose_name = 'Обращение'
        verbose_name_plural = 'Обращения'

    def get_absolute_url(self):
        return reverse('FeedbackForm')
        
    
    def __str__(self):
        return self.text