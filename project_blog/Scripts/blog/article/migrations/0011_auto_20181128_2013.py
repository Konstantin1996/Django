# Generated by Django 2.1.3 on 2018-11-28 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0010_auto_20181127_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_image',
            field=models.ImageField(blank=True, upload_to='articleimages', verbose_name='Картинка'),
        ),
    ]