from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view()),
    path('<slug:category_slug>/', views.PostListView.as_view(), name="category"),
    path('<slug:category>/<slug:slug>/', views.PostDetailView.as_view(), name="detail_post"),
    path('tag/<slug:slug>/', views.PostListView.as_view(), name='tag_list'),
]
