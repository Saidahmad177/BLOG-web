from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .forms import CommentsForm
from .models import New, Comments
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

    def post(self, request, slug):
        blog_name = New.published.get(slug=slug)
        form = CommentsForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.blog=blog_name
            new_comment.user=request.user
            new_comment.save()

            return redirect(reverse('blog:blog_detail_view', kwargs={'slug': slug}))

        return render(request, 'blog/blog_detail.html')


def about_page(request):
    return render(request, 'blog/about.html')


def gallery_page(request):
    return render(request, 'blog/gallery.html')


def contact_page(request):
    return render(request, 'blog/contact.html')
