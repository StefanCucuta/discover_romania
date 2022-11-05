from . import views
from django.urls import path
from .views import CreatePostView, UpdatePostView, DeletePostView

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('detail/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('post/new/', views.CreatePostView.as_view(), name='post_create'),

    path('<slug:slug>/update/', UpdatePostView.as_view(), name='post-update'),
    path('<slug:slug>/delete/', DeletePostView.as_view(), name='post-delete'),
]
