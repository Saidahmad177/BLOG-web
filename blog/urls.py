from django.urls import path
from .views import HomeView, about_page, gallery_page, contact_page, BlogDetailView

app_name = 'blog'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', about_page, name='about'),
    path('gallery/', gallery_page, name='gallery'),
    path('contact/', contact_page, name='contact'),
    path('<slug:slug>/', BlogDetailView.as_view(), name='blog_detail_view'),

]
