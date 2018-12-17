from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Article(models.Model):
    article_title = models.CharField('Заголовок',max_length=200,help_text='Введите заголовок статьи')
    article_text = models.TextField('Текст статьи',help_text='Введите текст статьи')
    article_date = models.DateTimeField('Дата')
    article_likes = models.IntegerField('Количество лайков',default=0)
    article_image = models.ImageField('Картинка', upload_to='articleimages', blank=True, null=True)
    class Meta():
        db_table = 'article'
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.article_title

class Comments(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comments_date = models.DateTimeField(default=timezone.now)
    comments_from = models.ForeignKey(User, on_delete=models.CASCADE)
    comments_text = models.TextField('Текст комментария')

    class Meta():
        db_table = 'comments'
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.comments_text