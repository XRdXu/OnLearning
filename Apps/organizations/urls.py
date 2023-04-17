import django

from Apps.organizations.views import OrgView, OrgHomeView, InstructorsListView, InstructorHomeView

from django.conf.urls import url


urlpatterns = [
    url(r'list/$', OrgView.as_view(), name="list"),
    url(r'(?P<org_id>\d+)/$', OrgHomeView.as_view(), name="home"),
    url(r'instructors/$', InstructorsListView.as_view(), name="instructors"),
    url(r'instructors/(?P<instructor_id>\d+)/$', InstructorHomeView.as_view(), name="instructor_detail"),
]