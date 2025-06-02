from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('classes/', views.classes, name='classes'),
    path('gallery/', views.gallery, name='gallery'),
    path('membership/', views.membership, name='membership'),
    path('contact/', views.contact, name='contact'),
    path('trainers/', views.trainers, name='trainers'),
    path('notifications/', views.notifications, name='notifications'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),


]