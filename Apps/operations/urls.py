import django

from django.conf.urls import url

from Apps.operations.views import CommentView

urlpatterns = [
    url(r'comment/$', CommentView.as_view(), name="comment"),
]