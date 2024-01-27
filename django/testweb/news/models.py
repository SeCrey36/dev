from django.db import models

# Create your models here.
class Articles(models.Model):
    title = models.CharField('Название', max_length=50, default='news_title')
    anons = models.CharField('Анонс', max_length=250, default='news_title')
    full_text = models.TextField('Полный текст')
    date = models.DateField('Дата публикации')

    def __str__(self):
        return self.title