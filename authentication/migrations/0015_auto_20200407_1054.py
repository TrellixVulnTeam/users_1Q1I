# Generated by Django 3.0.2 on 2020-04-07 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0014_auto_20200402_0547'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneNumberOtp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otp', models.IntegerField(default=6438)),
                ('phone', models.CharField(max_length=30, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='userotp',
            name='otp',
            field=models.IntegerField(default=2536),
        ),
    ]