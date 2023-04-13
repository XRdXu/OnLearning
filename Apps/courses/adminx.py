import xadmin

from Apps.courses.models import Course, Lesson, Video, CourseResources


class GlobalSettings(object):
    site_title = "OnlineCoursePlatform_ManagementSystem"
    site_footer = "OnlineCoursePlatform"


class BaseSettings(object):
    enable_themes = True
    use_bootswatch = True


class CourseAdmin(object):
    list_display = ["name", "desc", "course_detail", "difficulty", "duration", "number_of_students"]
    search_fields = ["name", "desc", "course_detail", "difficulty", "number_of_students"]
    list_filter = ["name", "desc", "course_detail", "difficulty", "number_of_students"]
    list_editable = ["difficulty", "desc"]


class LessonAdmin(object):
    list_display = ['course', 'name', 'duration']
    search_fields = ['course', 'name']
    list_filter = ['course__name', 'name', 'duration']


class VideoAdmin(object):
    list_display = ['Lesson', 'name', 'duration']
    search_fields = ['Lesson', 'name']
    list_filter = ['Lesson', 'name', 'duration']


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'file']
    search_fields = ['course', 'name', 'file']
    list_filter = ['course', 'name', 'file']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResources, CourseResourceAdmin)

xadmin.site.register(xadmin.views.CommAdminView, GlobalSettings)
xadmin.site.register(xadmin.views.BaseAdminView, BaseSettings)
