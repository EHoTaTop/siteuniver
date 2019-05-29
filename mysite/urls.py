from django.urls import path
from .import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^teachers/$', views.TeacherListView.as_view(), name='teachers'),
    url(r'^teachers/(?P<pk>\d+)$', views.teacher_detail, name='teacher-detail'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
