from django.urls import path
from .views import *

urlpatterns = [
    path("list/", CommissionListView.as_view(), name="list"),
    path("detail/<int:pk>/", CommissionDetailView.as_view(), name="comm-detail"),
]

app_name = "commisions"
