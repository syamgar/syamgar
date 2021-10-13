from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('report/', views.report),
    path('tlogin/', views.tLogin),
    path('slogin/', views.sLogin),
]
