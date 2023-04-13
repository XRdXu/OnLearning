from django.db import models

from Apps.users.models import BasedModel


class Organizations(BasedModel):
    name = models.CharField(verbose_name="Name of the organization", max_length=50)
    desc = models.TextField(verbose_name="Description", max_length=5000, default="")
    desc_short = models.TextField(verbose_name="ShortDescription", max_length=200, default="")
    web_url = models.TextField(verbose_name="WebUrl", max_length=200, default="")
    tag = models.CharField(verbose_name="Organization tag", max_length=20, default="")
    category = models.CharField(verbose_name="category", max_length=20, choices=(("Study channel", "Study channel"), ("Instructions", "Instructions"), ("Schools", "Schools")))
    click_nums = models.IntegerField(verbose_name="Number of clicks", default=0)
    number_of_beFav = models.IntegerField(verbose_name="number of students who likes the organization", default=0)
    image = models.ImageField(upload_to="org/%Y/%m", verbose_name="Logo", max_length=100)
    number_of_students = models.IntegerField(verbose_name="number of students", default=0)
    address = models.CharField(max_length=150, verbose_name="address", default="")
    number_of_courses = models.IntegerField(verbose_name="num of courses", default=0)

    def courses(self):
        courses = self.course_set.filter(is_classics=True)[:3]
        return courses

    class Meta:
        verbose_name = "Organizations"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Instructors(BasedModel):
    org = models.ForeignKey(Organizations, on_delete=models.CASCADE, verbose_name="From org")
    name = models.CharField(verbose_name="Name of the instructor", max_length=50)
    desc = models.TextField(verbose_name="Description", max_length=5000, default="")
    work_position = models.CharField(max_length=50, verbose_name="position", default="")
    click_nums = models.IntegerField(default=0, verbose_name="num of clicks")
    fav_nums = models.IntegerField(default=0, verbose_name="number of been collected")
    image = models.ImageField(upload_to="teacher/%Y/%m", verbose_name="profile photo", max_length=100, default="")

    class Meta:
        verbose_name = "Instructors"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


