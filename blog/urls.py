from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    # path('', views.home, name='home'),
    path('header', views.header, name='header'),
    path('footer', views.footer, name='footer'),
]