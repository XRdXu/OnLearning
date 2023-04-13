from django.shortcuts import render
from django.views.generic.base import View
from Apps.organizations.models import Organizations
from WebOnlineCourse.settings import MEDIA_URL


class OrgHomeView(View):
    def get(self, request, org_id, *args, **kwargs):
        course_orgs = Organizations.objects.filter(id = int(org_id))
        course_org = course_orgs[0]
        course_org.click_nums += 1
        course_org.save()

        all_courses = course_org.course_set.all()
        all_teacher = course_org.instructors_set.all()

        return render(request, "org_page.html",{
            "all_courses":all_courses,
            "all_teacher":all_teacher,
            "course_org":course_org
        })


class OrgView(View):
    def get(self, request, *args, **kwargs):
        all_orgs = Organizations.objects.all()
        return render(request, "org_list.html", {
            "all_orgs": all_orgs,
        })
