from django.shortcuts import render
from django.views.generic.base import View
from Apps.courses.models import Course, CourseResources
from django.contrib.auth.mixins import LoginRequiredMixin
from Apps.operations.models import UserCourseRelation, CourseComments


class CourseDetailView(View):
    def get(self, request, course_id, *args, **kwargs):
        course = Course.objects.get(id=int(course_id))
        course.number_of_clicks += 1
        course.save()

        return render(request, "course_page.html", {
            "course": course
        })


class CourseCommentView(LoginRequiredMixin, View):
    login_url = "/login/"

    def get(self, request, course_id, *args, **kwargs):
        course = Course.objects.get(id=int(course_id))
        course.number_of_clicks += 1
        course.save()

        comments = CourseComments.objects.filter(course=course)

        user_course = UserCourseRelation.objects.filter(user=request.user, course=course)
        if not user_course:
            user_course = UserCourseRelation(user=request.user, course=course)
            user_course.save()

            course.number_of_students += 1
            course.save()

        course_resource = CourseResources.objects.filter(course=course)

        return render(request, "course-comment.html", {
            "course": course,
            "course_resource": course_resource,
            "comments": comments
        })


class CourseLessonView(LoginRequiredMixin, View):
    login_url = "/login/"

    def get(self, request, course_id, *args, **kwargs):
        course = Course.objects.get(id=int(course_id))
        course.number_of_clicks += 1
        course.save()

        user_course = UserCourseRelation.objects.filter(user=request.user, course=course)
        if not user_course:
            user_course = UserCourseRelation(user=request.user, course=course)
            user_course.save()

            course.number_of_students += 1
            course.save()

        course_resource = CourseResources.objects.filter(course=course)

        return render(request, "course-video.html", {
            "course": course,
            "course_resource": course_resource
        })
