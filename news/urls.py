from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('accounts/profile/', views.post_list, name='post_list'),
    path('post/list/', views.post_list, name='post_list2'),
    path('post/new/', views.post_new, name='post_new'),
]