from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Product


class MerchListView(ListView):
    model = Product
    template_name = "product_list.html"


class MerchDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "product_detail.html"
