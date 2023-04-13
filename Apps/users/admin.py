from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from Apps.users.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    pass


admin.site.register(UserProfile, UserAdmin)
