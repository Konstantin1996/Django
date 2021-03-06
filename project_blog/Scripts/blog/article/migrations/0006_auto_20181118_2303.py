# Generated by Django 2.1.3 on 2018-11-18 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_auto_20181118_2234'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
        migrations.AlterField(
            model_name='article',
            name='article_text',
            field=models.TextField(help_text='Введите текст статьи', verbose_name='Текст статьи'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='comments_text',
            field=models.TextField(verbose_name='Текст комментария'),
        ),
    ]
