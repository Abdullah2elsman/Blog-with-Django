from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts', views.post_list, name='posts'),
    path('posts/<slug:slug>/', views.post_detail, name='post_detail'),
    path('posts/<slug:slug>/edit/', views.post_edit, name='post_edit'),
    path('posts/<slug:slug>/delete/', views.post_delete, name='post_delete'),
]