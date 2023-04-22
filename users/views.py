from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from users.forms import RegisterForm, ProfileForm


class UserRegisterView(View):
    def get(self, request):
        return render(request, 'users/register.html')

    def post(self, request):
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully registered.')

            return redirect(reverse('users:login'))

        return render(request, 'users/register.html', {'form': form})


class UserLoginView(View):
    def get(self, request):
        return render(request, 'users/login.html')

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            messages.success(request, 'You have successfully login')
            return redirect(reverse('blog:home'))

        messages.info(request, 'Wrong username and password', extra_tags='danger')
        return redirect(reverse('users:login'))


def user_logout(request):
    logout(request)
    messages.info(request, 'You have logged in')

    return redirect(reverse('blog:home'))


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        form = ProfileForm(instance=request.user)

        return render(request, 'users/profile.html', {'form': form})

    def post(self, request):
        form = ProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully profile update')

            return redirect(reverse('users:profile'))

        return  render(request, 'users/profile.html', {'form': form})


