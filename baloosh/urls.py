from django.urls import path
from . import views

urlpatterns = [
    path ('', views.home),
    path('about/', views.about),
    path('accomodation/', views.accomodation),
    path('gallery/', views.gallery),
    path('contact/', views.contactus),
    path('signout/', views.signout),
]