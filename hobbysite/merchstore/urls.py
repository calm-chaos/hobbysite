from django.urls import path
from .views import MerchListView, MerchDetailView

urlpatterns = [
    path("items/", MerchListView.as_view(), name="products"),
    path("item/<int:pk>/", MerchDetailView.as_view(), name="product-detail"),
]

app_name = "merchstore"
