from django.db import models

from django.contrib.auth import get_user_model

from Apps.users.models import BasedModel

from Apps.courses.models import Course

UserProfile = get_user_model()


class UserConsultation(BasedModel):
    name = models.CharField(max_length=20, verbose_name="user name")
    phone_number = models.CharField(max_length=11, verbose_name="phone number")
    course_name = models.CharField(max_length=50, verbose_name="course_name")

    class Meta:
        verbose_name = "User Consultation"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{name}_{course}({phone_number})".format(name=self.name, course=self.course_name, phone_number=self.phone_number)


class CourseComments(BasedModel):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="user info")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="course")
    comments = models.CharField(max_length=200, verbose_name="comments")

    class Meta:
        verbose_name = "comments"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.comments


class UserFavorites(BasedModel):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="user")
    fav_id = models.IntegerField(verbose_name="type id")
    fav_type = models.IntegerField(choices=((1, "course"), (2, "instruction"), (3, "instructor")), default=1, verbose_name="收藏类型")

    class Meta:
        verbose_name = "user favorites"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{user}_{id}".format(user=self.user, id=self.user_id)


class UserMessage(BasedModel):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="user info")
    message = models.CharField(max_length=200, verbose_name="contents")
    has_read = models.BooleanField(default=False, verbose_name="whether the message has been read")

    class Meta:
        verbose_name = "user message"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.message


class UserCourseRelation(BasedModel):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="user")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="course")

    class Meta:
        verbose_name = "user course relation"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.course.name


