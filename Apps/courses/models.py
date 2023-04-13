

from django.db import models

from Apps.users.models import BasedModel

from Apps.organizations.models import Instructors,Organizations

# Requirements of designing course table
# Operations between courses,lessons,video tutorials,and resources


class Course(BasedModel):
    instructor = models.ForeignKey(Instructors, null=True,blank=True, on_delete=models.CASCADE, verbose_name="Instructor")
    course_org = models.ForeignKey(Organizations, null=True, blank=True, on_delete=models.CASCADE, verbose_name="Organization")
    name = models.CharField(verbose_name="course name", max_length=50)
    desc = models.CharField(verbose_name="course description", max_length=300)
    duration = models.IntegerField(verbose_name="duration of the course(mins)", default=0)
    difficulty = models.CharField(verbose_name="difficulty", choices=(("beginner", "beginner"), ("intermediate", "intermediate"), ("hard", "hard")), max_length= 12)
    number_of_students = models.IntegerField(verbose_name="number of students", default=0)
    number_of_beFav = models.IntegerField(verbose_name="number of students who intended to take the course",default=0)
    number_of_clicks = models.IntegerField(verbose_name="number_of_clicks", default=0)
    announcement = models.CharField(verbose_name="course announcement", max_length=300, default="")
    category = models.CharField(verbose_name="category", max_length=20)
    tag = models.CharField(verbose_name="course tag",max_length=10)
    shoud_know = models.CharField(verbose_name="should know ahead taking the course", max_length=300,default='')
    teacher_desc = models.CharField(verbose_name="what the teacher wants to say", max_length=300,default='')

    course_detail = models.TextField(verbose_name="course's details")
    Images = models.ImageField(upload_to="courses/%Y/%m", verbose_name="img", max_length=100)

    class Meta:
        verbose_name = "Class info"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Lesson(BasedModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="lesson name", max_length=100)
    duration = models.IntegerField(verbose_name="duration of the lesson(mins)", default=0)

    class Meta:
        verbose_name = "Lesson info"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Video(BasedModel):
    Lesson = models.ForeignKey(Lesson, verbose_name="sections", on_delete=models.CASCADE)
    name = models.CharField(verbose_name="video name", max_length=100)
    duration = models.IntegerField(verbose_name="duration of the video(mins)", default=0)
    url = models.CharField(max_length=200, verbose_name="video url")

    class Meta:
        verbose_name = "Video"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseResources(BasedModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="resource")
    name = models.CharField(verbose_name="name", max_length=100)
    file = models.FileField(verbose_name="downloading address", upload_to="course/resources/%y/%m", max_length=200)

    class Meta:
        verbose_name = "course resources"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
