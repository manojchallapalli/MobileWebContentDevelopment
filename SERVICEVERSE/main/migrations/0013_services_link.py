# Generated by Django 3.1.4 on 2021-03-23 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20210318_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='link',
            field=models.CharField(default='url', max_length=500),
        ),
    ]