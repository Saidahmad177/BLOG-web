from django.shortcuts import render, get_object_or_404
from .models import New
from django.views.generic import View


class HomeView(View):
    def get(self, request):
        data = New.published.all()
        context = {
            'data': data,
        }

        return render(request, 'blog/home.html', context)


class BlogDetailView(View):
    def get(self, request, slug):
        post = New.published.get(slug=slug)
        context = {
            'post_item':post,
        }

        return render(request, 'blog/blog_detail.html', context)


def about_page(request):
    return render(request, 'blog/about.html')


def gallery_page(request):
    return render(request, 'blog/gallery.html')


def contact_page(request):
    return render(request, 'blog/contact.html')
