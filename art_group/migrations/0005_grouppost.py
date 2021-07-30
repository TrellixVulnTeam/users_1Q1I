# Generated by Django 3.0.2 on 2021-07-13 08:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('art_group', '0004_postcomment'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=250)),
                ('thumbnil', models.FileField(blank=True, null=True, upload_to='')),
                ('second_img', models.FileField(blank=True, null=True, upload_to='')),
                ('third_img', models.FileField(blank=True, null=True, upload_to='')),
                ('upload_time', models.DateTimeField(auto_now=True)),
                ('comment', models.ManyToManyField(blank=True, related_name='users_comment', to='art_group.PostComment')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='art_group.Group')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]