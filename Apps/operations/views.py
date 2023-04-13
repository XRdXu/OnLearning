from django.shortcuts import render
from django.views.generic.base import View
from django.shortcuts import render
from Apps.operations.form import CommentsForm
from Apps.operations.models import CourseComments
from Apps.courses.models import Course
from django.http import JsonResponse

class CommentView(View):
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return JsonResponse({
                "status":"fail",
                "msg":"Not yet logged in"
            })

        comment_form = CommentsForm(request.POST)
        if comment_form.is_valid():
            course = comment_form.cleaned_data["course"]
            comments = comment_form.cleaned_data["comments"]

            comment = CourseComments()
            comment.user = request.user
            comment.comments = comments
            comment.course = course
            comment.save()

            return JsonResponse({
                "status": "success",
            })
        else:
            return JsonResponse({
                "status": "fail",
                "msg": "Param error"
            })


class IndexView(View):
    def get(self,request, *args, **kwargs):
        all_courses = Course.objects.all()
        return render(request, "index.html",{
            "all_courses": all_courses
        })
