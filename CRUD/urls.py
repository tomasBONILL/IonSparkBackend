from django.urls import path
from . import views

urlpatterns = [
    path('api/posts/', views.posts_api, name='posts_api')
]
