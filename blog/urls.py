from django.urls import path
from .views import (
    BlogsListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

urlpatterns = [
    path("post/<int:pk>", PostDetailView.as_view(), name="post_detail"),
    path("post/new", PostCreateView.as_view(), name="post-new"),
    path("post/<int:pk>/edit", PostUpdateView.as_view(), name="post_edit"),
    path("post/<int:pk>/delete", PostDeleteView.as_view(), name="post_delete"),
    path("", BlogsListView.as_view(), name="home"),
]
