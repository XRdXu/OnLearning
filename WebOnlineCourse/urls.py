"""WebOnlineCourse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.views.static import serve
from WebOnlineCourse.settings import MEDIA_ROOT

import xadmin

from Apps.users.views import LoginView, LogoutView, RegisterView
from Apps.organizations.views import OrgView, InstructorsListView
from Apps.operations.views import IndexView

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    path('', IndexView.as_view(), name="index"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('register/', RegisterView.as_view(), name="register"),
    path('captcha/', include('captcha.urls')),
    url(r'^media/(?P<path>.*$)', serve, {"document_root": MEDIA_ROOT}),

    url(r'org/', include(('Apps.organizations.urls', "organization"), namespace="org")),

    url(r'course/', include(('Apps.courses.urls', "courses"), namespace="course")),

    url(r'^op/', include(('Apps.operations.urls', "operations"), namespace="op")),

    url(r'instructors/', include(('Apps.organizations.urls', "instructors"), namespace="instructors")),

    url(r'users/', include(('Apps.users.urls', "users"), namespace="users")),
]


