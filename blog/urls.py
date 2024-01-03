from django.urls import path
from .views import BlogsListView, PostDetailView

urlpatterns = [
    path("", BlogsListView.as_view(), name="home"),
    path("post/<int:pk>", PostDetailView.as_view(), name="post_detail"),
]
