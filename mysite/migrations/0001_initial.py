# Generated by Django 2.1.7 on 2019-04-24 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='photo_teachers/')),
                ('fio', models.CharField(max_length=40)),
                ('cabinet', models.IntegerField(max_length=3)),
                ('email', models.EmailField(max_length=254)),
                ('description', models.TextField(max_length=150)),
            ],
        ),
    ]
