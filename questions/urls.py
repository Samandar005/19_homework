from django.urls import path
from . import views


app_name = 'questions'

urlpatterns = [
    path('create/test/', views.create_test, name='create'),
    path('list/', views.test_list, name='list'),
    path('delete/<int:pk>/', views.delete, name='delete'),
]