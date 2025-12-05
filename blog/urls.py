from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    # ↓ この行を追加！ <int:pk> は「記事のID番号」という意味です
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]