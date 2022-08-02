from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('login/', views.home_login),
    path('register/', views.home_register),
    path('about/', views.about),
    path('accomodation/', views.accomodation),
    path('gallery/', views.gallery),
    path('contact/', views.contactus),
    path('signout/', views.signout),
]