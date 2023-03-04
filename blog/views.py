from django.shortcuts import render
from django.views.generic import ListView
from .models import Yangilik


# Create your views here.
class HomePageView(ListView):
    model = Yangilik
    template_name = 'home.html'
    context_object_name = 'News_data'


def about_page(request):
    return render(request, 'blog/about.html')
