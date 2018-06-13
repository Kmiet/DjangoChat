from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.lobby),
    path('channel/', views.channel),
    path('user/settings', views.settings),
    path('channel/<int:id>/', views.chat)
]