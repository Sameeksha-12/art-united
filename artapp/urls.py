from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('signup/',views.signup,name='signup'),
    path('signin/',views.signin,name='signin'),
    path('home/',views.home,name='home'),
    path('create/', views.create_blog, name='create_blog'), 
    path('explore/',views.explore,name='explore'),
    path('show/<int:blog_id>/',views.show,name='show'),
    path('artwork/<str:username>/', views.user_artwork, name='user_artwork'),
]

