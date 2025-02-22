from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('competitions/', views.competitions, name='competitions'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('contactus/', views.contactus, name='contactus'),

]