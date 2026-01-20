"""
URL configuration for WEB_UOK project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('', views.home, name='home'), 
    path('water-factory/', views.water_factory, name='water_factory'),
    path('herbal-factory/', views.herbal_factory, name='herbal_factory'),     # <-- ตัวนี้คือตัวที่แจ้ง Error อยู่
    path('cosmetic-factory/', views.cosmetic_factory, name='cosmetic_factory'),
    path('resort/', views.resort, name='resort'),
    path('room-detail/', views.room_detail, name='room_detail'),
    path('room/1a/', views.room_detail, name='room_detail'),
    path('room-2a/', views.room_2a_view, name='room_2a'),
    path('room-3a/', views.room_3a_view, name='room_3a'),
    path('room-4a/', views.room_4a_view, name='room_4a'),
    path('room-5a/', views.room_5a_view, name='room_5a'),
]

