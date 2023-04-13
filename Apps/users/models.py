from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


GENDERS_CHOICES = (
    ("male", "Male"),
    ("female", "Female")
)


class BasedModel(models.Model):
    added_time = models.DateTimeField(default=datetime.now, verbose_name="course added time")

    class Meta:
        abstract = True


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name="nick_name", default="")
    birthday = models.DateField(verbose_name="Birthday", null=True, blank=True)
    gender = models.CharField(verbose_name="gender", choices=GENDERS_CHOICES, max_length=6)
    address = models.CharField(max_length=100, verbose_name="Address", default="")
    mobile = models.CharField(max_length=11, verbose_name="PhoneNumber")
    Image = models.ImageField(upload_to="head_image/%Y/%m", default="default.jpg")

    class Meta:
        verbose_name = "UserInfo"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
