from django.conf.urls import *

from django.views.generic.base import TemplateView
from aspc.courses.views import CourseDetailView, DepartmentListView, DepartmentCoursesView

urlpatterns = patterns('',
    (r'^search/$', 'aspc.courses.views.search'),
    (r'^schedule/$', 'aspc.courses.views.schedule'),
    url(r'^schedule/(?P<course_code>[\w\d-]+)/add/$', 'aspc.courses.views.schedule_course_add', name="course_add"),
    url(r'^schedule/(?P<course_code>[\w\d-]+)/remove/$', 'aspc.courses.views.schedule_course_remove', name="course_remove"),
    (r'^schedule/(?P<schedule_id>\d+)/$', 'aspc.courses.views.view_schedule'),
    (r'^schedule/(?P<schedule_id>\d+)/minimal/$', 'aspc.courses.views.view_minimal_schedule'),
    (r'^schedule/(?P<schedule_id>\d+)/icalendar/$', 'aspc.courses.views.ical_export'),
    (r'^schedule/icalendar/$', 'aspc.courses.views.ical_export'),
    (r'^schedule/load/$', 'aspc.courses.views.load_from_session'),
    (r'^schedule/clear/$', 'aspc.courses.views.clear_schedule'),
    (r'^schedule/save/$', 'aspc.courses.views.share_schedule'),
    url(r'^browse/$', DepartmentListView.as_view(), name="department_list"),
    url(r'^browse/(?P<slug>[A-Z]+)/$', DepartmentCoursesView.as_view(), name="department_detail"),
    url(r'^browse/(?P<dept>[A-Z]+)/(?P<course_code>[\w\d-]+)/$', CourseDetailView.as_view(), name="course_detail"),
    url(r'^$', TemplateView.as_view(template_name='courses/landing.html'), name="coursesearch_home"),
)
