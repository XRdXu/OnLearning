import django

from Apps.courses.views import CourseDetailView, CourseLessonView,CourseCommentView

from django.conf.urls import url


urlpatterns = [
    url(r'(?P<course_id>\d+)/$', CourseDetailView.as_view(), name="detail"),
    url(r'(?P<course_id>\d+)/lesson/$', CourseLessonView.as_view(), name="lesson"),
    url(r'(?P<course_id>\d+)/comments/$', CourseCommentView.as_view(), name="comments"),
]