from django.contrib import admin
from django.urls import path, include
# from wish import views

# from django.conf import settings
# from django.conf.urls import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', include('blog.urls'), name='blog_urls'),
    path('accounts/', include('allauth.urls')),
    path('wish/', include('wish.urls')),
]