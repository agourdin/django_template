from django.urls import include, path

from app import views

urlpatterns = [
    path('', views.home, name='home.html'),
]
