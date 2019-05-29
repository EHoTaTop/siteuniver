# Generated by Django 2.1.7 on 2019-05-08 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0009_auto_20190425_0341'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a teachers discipline (e.g. Physics, Mathematics etc.)', max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='cabinet',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='description',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='email',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='name',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='photo',
        ),
        migrations.AddField(
            model_name='teacher',
            name='Teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mysite.Teacher'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='img',
            field=models.ImageField(blank=True, default='avatars/empty.jpg', null=True, upload_to='avatars/'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='summary',
            field=models.TextField(default='', help_text='Enter a brief description of the Teacher', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='Discipline',
            field=models.ManyToManyField(help_text='Select a genre for this book', to='mysite.Discipline'),
        ),
    ]