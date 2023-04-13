from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from Apps.users.forms import RegisterForm
from Apps.users.models import UserProfile
from django.contrib.auth.hashers import make_password


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

