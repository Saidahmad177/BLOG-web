from django.shortcuts import render
from .models import New


def about_page(request):
    return render(request, 'blog/about.html')


def gallery_page(request):
    pass


def contact_page(request):
    pass
