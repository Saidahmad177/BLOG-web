from django.urls import path
from .views import HomePageView, about_page, gallery_page

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', about_page, name='about'),
    path('gallery/', gallery_page, name='gallery'),

]