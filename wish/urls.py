from django.urls import path
from . import views


urlpatterns = [
 path('', views.create_wish, name="wish_create"),
 path('delete/<wish_id>/', views.delete, name="delete"),
 path('cross_off/<wish_id>/', views.cross_off, name="cross_off"),
 path('uncross/<wish_id>/', views.uncross, name="uncross"),
  ]
