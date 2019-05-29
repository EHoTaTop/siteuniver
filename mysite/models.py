from django.db import models
from django.urls import reverse

class Discipline(models.Model):
    name = models.CharField(max_length=200, help_text="Enter a teachers discipline (e.g. Physics, Mathematics etc.)")

    def __str__(self):
        return self.name


class Teacher(models.Model):
    title = models.CharField(max_length=100, verbose_name="Ф.И.О")
    position = models.CharField(max_length=100, verbose_name="Должность")
    summary = models.TextField(max_length=3000, help_text="Enter a brief description of the Teacher", verbose_name="Детальная информация")
    discipline = models.ManyToManyField(Discipline, help_text="Select a discipline for this teacher", verbose_name="Дисциплина")
    img = models.ImageField(upload_to="avatars/", null=True, blank=True, default="avatars/empty.jpg", verbose_name="Фотография")

    def __str__(self):
        return  self.title


    def get_absolute_url(self):
        return reverse('teacher-detail', args=[str(self.id)])

    def display_discipline(self):
        return ', '.join([ discipline.name for discipline in self.discipline.all()[:2] ])
    display_discipline.short_description = 'Discipline'
