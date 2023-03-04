from django.urls import path
from .views import HomePageView, about_page

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', about_page, name='about'),

]