from django.urls import path
from .views import *

urlpatterns = [
    path("threads/", ForumListView.as_view(), name="threads"),
    path("thread/<int:pk>", ForumDetailView.as_view(), name="thread-detail"),
]

app_name = "forum"
