from django.shortcuts import render
from .models import Teacher, Discipline
from django.views import generic


def home(request):
    return render(request, "home.html")


class TeacherListView(generic.ListView):
    model = Teacher
    paginate_by = 10

class TeacherDetailView(generic.DetailView):
    model = Teacher

def teacher_detail(request, pk):
    teacher_id = Teacher.objects.get(pk=pk)
    return render(request, 'mysite/teacher_detail.html', context={"Teacher":teacher_id})
