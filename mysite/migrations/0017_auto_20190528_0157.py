# Generated by Django 2.1.7 on 2019-05-27 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0016_auto_20190528_0101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='summary',
            field=models.TextField(help_text='Enter a brief description of the Teacher', max_length=3000, verbose_name='Детальная информация'),
        ),
    ]