from django.urls import path
from . import views


app_name = 'questions'

urlpatterns = [
    path('create/test/', views.create_test, name='create'),
    path('update/test/<int:pk>/', views.update_test, name='update'),
    path('list/', views.test_list, name='list'),
    path('delete/<int:pk>/', views.delete, name='delete'),
]