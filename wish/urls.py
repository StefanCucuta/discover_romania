from django.urls import path
from . import views


urlpatterns = [
 path('', views.create_wish, name="wish_create"),
]