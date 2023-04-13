import xadmin

from Apps.operations.models import UserConsultation, CourseComments, UserFavorites, UserMessage, UserCourseRelation


class UserConsultationAdmin(object):
    list_display = ['name', 'phone_number', 'course_name']
    search_fields = ['name', 'phone_number', 'course_name']
    list_filter = ['name', 'phone_number', 'course_name']


class UserCourseRelationAdmin(object):
    list_display = ['user', 'course']
    search_fields = ['user', 'course']
    list_filter = ['user', 'course']


class UserMessageAdmin(object):
    list_display = ['user', 'message', 'has_read']
    search_fields = ['user', 'message', 'has_read']
    list_filter = ['user', 'message', 'has_read']


class CourseCommentsAdmin(object):
    list_display = ['user', 'course', 'comments']
    search_fields = ['user', 'course', 'comments']
    list_filter = ['user', 'course', 'comments']


class UserFavoritesAdmin(object):
    list_display = ['user', 'fav_id', 'fav_type']
    search_fields = ['user', 'fav_id', 'fav_type']
    list_filter = ['user', 'fav_id', 'fav_type']


xadmin.site.register(UserConsultation, UserConsultationAdmin)
xadmin.site.register(CourseComments, CourseCommentsAdmin)
xadmin.site.register(UserFavorites, UserFavoritesAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(UserCourseRelation, UserCourseRelationAdmin)

