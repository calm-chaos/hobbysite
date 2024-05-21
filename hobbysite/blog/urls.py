from django.urls import path
from .views import *

urlpatterns = [
    path("articles/", BlogListView.as_view(), name="articles"),
    path("article/<int:pk>", BlogDetailView.as_view(), name="article-detail"),
]

app_name = "blog"
