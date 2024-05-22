from django.urls import path
from .views import WikiDetailView, WikiListView

urlpatterns = [
    path("articles/", WikiListView.as_view(), name="articles"),
    path("article/<int:pk>/", WikiDetailView.as_view(), name="article-detail"),
]

app_name = "wiki"
