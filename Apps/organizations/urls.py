import django

from Apps.organizations.views import OrgView, OrgHomeView

from django.conf.urls import url


urlpatterns = [
    url(r'list/$', OrgView.as_view(), name="list"),
    url(r'(?P<org_id>\d+)/$', OrgHomeView.as_view(), name="home")
]