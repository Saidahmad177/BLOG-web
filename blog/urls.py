from django.urls import path
from .views import HomeView, about_page, ContactView, BlogDetailView

app_name = 'blog'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', about_page, name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('<slug:slug>/', BlogDetailView.as_view(), name='blog_detail_view'),

]
