from django.views.generic import View
from blog.models import New
from django.shortcuts import render


class HomeView(View):
    def get(self, request):
        data = New.published.all()
        context = {
            'data': data,
        }

        return render(request, 'home.html', context)
