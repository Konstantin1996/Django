# Generated by Django 2.1.3 on 2018-11-27 14:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_auto_20181118_2303'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='comments_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 27, 14, 33, 33, 377290, tzinfo=utc)),
        ),
    ]
