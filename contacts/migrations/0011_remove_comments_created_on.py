# Generated by Django 3.0.2 on 2020-11-24 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0010_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='created_on',
        ),
    ]