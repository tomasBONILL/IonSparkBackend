from django.urls import path
from .views import posts_api, register_api

urlpatterns = [
    path('posts/', posts_api),
    path('register/', register_api),
]
