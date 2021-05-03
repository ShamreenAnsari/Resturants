from django.contrib import admin
from django.urls import path,include
from.import views
urlpatterns = [
    path('',views.index,name='index'),
    path('about_us/',views.about_us,name='about_us'),
    path('menus/',views.menus,name='menus'),
    # path('admin/',views.login,name='login'),
    # path('upload/',views.upload,name='upload'),
]