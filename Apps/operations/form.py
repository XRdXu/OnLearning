import re

from django import forms
from Apps.operations.models import CourseComments


class CommentsForm(forms.ModelForm):
    class Meta:
        model = CourseComments
        fields = ["course", "comments"]