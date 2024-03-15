from django.urls import path
from . import views

# определяется именное пространство с помощью переменной app_name
app_name = 'blog'

urlpatterns = [
    # представления поста
    path('', views.post_list, name='post_list'),
    path('<int:id>/', views.post_detail, name='post_detail'),
]