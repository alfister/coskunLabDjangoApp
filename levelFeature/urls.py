from django.urls import path
from . import views

urlpatterns = [
    path('get_list/', views.get_list, name='get_list'),
    path('get_reading/<int:pk>/', views.get_reading, name='get_reading'),
    path('post_reading/', views.post_reading, name='post_reading'),
    path('delete_reading/<int:pk>/', views.delete_reading, name='delete_reading'),
]