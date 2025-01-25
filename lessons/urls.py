from django.urls import path
from . import views


app_name = 'lessons'

urlpatterns = [
    path('create/', views.create_lesson, name='create'),
    path('list/', views.lesson_list, name='list'),
    path('list/<int:pk>/', views.update_lesson, name='update'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('delete/<int:pk>/', views.delete, name='delete'),

]