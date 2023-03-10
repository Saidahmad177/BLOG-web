from django.shortcuts import render
from django.views.generic import ListView
from .models import New


# Create your views here.
class HomePageView(ListView):
    model = New
    template_name = 'home.html'
    context_object_name = 'News_data'


# about page
def about_page(request):
    return render(request, 'blog/about.html')


def gallery_page(request):
    return render(request, 'blog/gallery.html')


def contact_page(request):
    return render(request, 'blog/contact.html')
