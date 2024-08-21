from django.urls import path
from . import views

urlpatterns = [
    # path('', views.post_list, name='post_list'),
    path('', views.home, name='home'),
    path('header/', views.header, name='header'),
    path('footer/', views.footer, name='footer'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
  
    path('pricing/', views.pricing, name='pricing'),
    path('child/', views.child, name='child'),
    path('young/', views.young, name='young'),
    path('audult/', views.audult, name='audult'),
]