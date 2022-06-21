from django.urls import path

from . import views

urlpatterns = [
    path('', views.Home, name="home"),
    path('api/quizes/', views.Quizes, name="api")
]
