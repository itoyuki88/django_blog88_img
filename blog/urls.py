from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.PostListView.as_view(), name='blog-home'),
    path('form/', views.PostCreateView.as_view(), name='post-form'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/delete', views.PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/update', views.PostUpdateView.as_view(), name='post-update'),
]

