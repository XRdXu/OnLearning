from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from Apps.users.forms import RegisterForm, UploadImageForm, UserInfoForm, ChangePwdForm
from Apps.users.models import UserProfile
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin


class ChangePwdView(View):
    def post(self, request, *args, **kwargs):
        pwd_form = ChangePwdForm(request.POST)
        if pwd_form.is_valid():
            pwd1 = request.POST.get("password1", "")
            pwd2 = request.POST.get("password2", "")
            if pwd1 != pwd2:
                return JsonResponse({
                    "status":"fail",
                    "msg": "Two passwords are not identical"
                })
            user = request.user
            user.set_password(pwd1)
            user.save()
            return JsonResponse({
                "status": "success",
            })
        else:
            return JsonResponse(pwd_form.errors)



class UploadImageView(LoginRequiredMixin, View):
    login_url = "/login/"

    def post(self, request, *args, **kwargs):
        image_form = UploadImageForm(request.POST, request.FILES, instance=request.user)
        if image_form.is_valid():
            image_form.save()
            print(image_form.errors)
            return JsonResponse({
                "status":"success"
            })
        else:
            return JsonResponse({
                "status": "fail"
            })


class UserInfoView(LoginRequiredMixin,View):
    login_url = "/login/"
    def get(self, request, *args, **kwargs):
        return render(request, "usercenter-info.html")
    def post(self, request, *args, **kwargs):
        user_info_form = UserInfoForm(request.POST, instance=request.user)
        if user_info_form.is_valid():
            user_info_form.save()
            return JsonResponse({
                "status": "success"
            })
        else:
            return JsonResponse(user_info_form.errors)



class RegisterView(View):
    def get(self, request, *args, **kwargs):
        register_form = RegisterForm()
        return render(request, "register.html", {'register_form':register_form})

    def post(self, request, *args, **kwargs):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            email = request.POST.get("email", "")
            password = request.POST.get("password", "")
            user_profile = UserProfile()
            user_profile.username = email
            user_profile.email = email
            user_profile.password = make_password(password)
            user_profile.save()
            return HttpResponseRedirect(reverse("login"))
        return render(request, "register.html")


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse("index"))


class LoginView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("index"))
        return render(request, "login.html")

    def post(self, request, *args, **kwargs):
        user_name = request.POST.get("username", "")
        password = request.POST.get("password", "")

        if not user_name:
            return render(request, "login.html", {"msg": "Please enter the username"})
        if not password:
            return render(request, "login.html", {"msg": "Please enter the password"})
        user = authenticate(username=user_name, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else: # did not find the user
            return render(request, "login.html", {"msg": "Either username or password is wrong or does not found"})

