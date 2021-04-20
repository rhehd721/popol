from django.urls import path, include
from . import views
from django.conf import settings    # media
from django.conf.urls.static import static    # media


urlpatterns = [
    path('', views.enter, name = "enter"),
    path('home/', views.home, name = "home"),
    path('introduce/', views.introduce, name = "introduce"),
    path('accept/', views.accept, name = "accept"),
    path('home/', views.guest, name = "guest"),
]
