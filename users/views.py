from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View


app_name = 'users'
class UserRegisterView(View):
    def get(self, request):
        return render(request, 'users/register.html')


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

