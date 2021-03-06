# Generated by Django 2.1.3 on 2018-11-18 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_auto_20181118_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_date',
            field=models.DateTimeField(verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_likes',
            field=models.IntegerField(default=0, verbose_name='Количество лайков'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_text',
            field=models.TextField(verbose_name='Текст статьи'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_title',
            field=models.CharField(help_text='Введите заголовок статьи', max_length=200, verbose_name='Заголовок'),
        ),
    ]
