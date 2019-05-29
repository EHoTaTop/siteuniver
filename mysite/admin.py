from django.contrib import admin
from .models import Teacher, Discipline


# admin.site.register(Teacher)
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_discipline')





admin.site.register(Discipline)
# Register your models here.
