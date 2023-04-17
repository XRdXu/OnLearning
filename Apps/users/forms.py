from django import forms
from captcha.fields import CaptchaField
from Apps.users.models import UserProfile


class UploadImageForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["Image"]


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
    captcha = CaptchaField()