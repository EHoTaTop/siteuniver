# Generated by Django 2.1.7 on 2019-04-25 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0006_auto_20190425_0313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=40, null=True, verbose_name='Ф.И.О'),
        ),
    ]
