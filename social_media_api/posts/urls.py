from django.urls import path
from .views import PostListView, PostCreateView, PostRetrieveUpdateDestroyView

urlpatterns = [
    path('feed/', PostListView.as_view(), name='post-feed'),
    path('posts/new/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', PostRetrieveUpdateDestroyView.as_view(), name='post-detail'),
]
