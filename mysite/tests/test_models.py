from django.test import TestCase
from mysite.models import Teacher

class TeacherModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Teacher.objects.create(title='Big')

    def test_title_label(self):
        teacher=Teacher.objects.get(id=1)
        field_label = teacher._meta.get_field('title').verbose_name
        self.assertEquals(field_label,'title')

    def test_position_label(self):
        teacher=Teacher.objects.get(id=1)
        field_label = teacher._meta.get_field('position').verbose_name
        self.assertEquals(field_label,'position')

    def test_title_max_length(self):
        teacher=Teacher.objects.get(id=1)
        max_length = teacher._meta.get_field('title').max_length
        self.assertEquals(max_length,100)


    def test_get_absolute_url(self):
        teacher=Teacher.objects.get(id=1)
        #This will also fail if the urlconf is not defined.
        self.assertEquals(teacher.get_absolute_url(),'/teachers/1')
