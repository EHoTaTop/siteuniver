from django.test import TestCase
from mysite.models import Teacher
from django.urls import reverse

class TeacherListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Create 13 authors for pagination tests
        number_of_teachers = 13
        for teacher_num in range(number_of_teachers):
            Teacher.objects.create(title='Christian %s' % teacher_num)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/teachers/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('teachers'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('teachers'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'mysite/teacher_list.html, base.html, navbar.html, footer.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('teachers'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['teacher_list']) == 10)

    def test_lists_all_authors(self):
        #Get second page and confirm it has (exactly) remaining 3 items
        resp = self.client.get(reverse('teachers')+'?page=2')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['teacher_list']) == 3)
