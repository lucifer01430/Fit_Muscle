from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('gallery/', views.gallery, name='gallery'),
    path('schedule/', views.schedule, name='schedule'),
    path('membership/', views.membership, name='membership'),
    path('trainers/', views.trainers, name='trainers'),
    path('contact/', views.contact, name='contact'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),  # Add blog detail URL
]