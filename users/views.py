from django.shortcuts import render
from django.views import View


app_name = 'users'
class UserRegisterView(View):
    def get(self, request):
        return render(request, 'users/register.html')


class UserLoginView(View):
    def get(self, request):
        return render(request, 'users/login.html')
