import django

from Apps.users.views import UserInfoView, UploadImageView

from django.conf.urls import url


urlpatterns = [
    url(r'info/$', UserInfoView.as_view(), name="info"),
    url(r'image/upload/$', UploadImageView.as_view(), name="image"),
]