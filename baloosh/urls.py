from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('login/', views.home_login),
    path('register/', views.home_register),
    path('userview/', views.userview),
    path('about/', views.about),
    path('accomodation/', views.accomodation),
    path('accomodation/', views.homeaccomodation),
    path('gallery/', views.gallery),
    path('contact/', views.contactus),
    path('signout/', views.signout),
]