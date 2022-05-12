from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.PostListView.as_view(), name='home'),
]

