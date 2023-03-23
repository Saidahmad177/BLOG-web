from django.urls import path
from .views import about_page, gallery_page, contact_page

app_name = 'blog'
urlpatterns = [
    path('about/', about_page, name='about'),
    path('gallery/', gallery_page, name='gallery'),
    path('contact/', contact_page, name='contact'),

]
