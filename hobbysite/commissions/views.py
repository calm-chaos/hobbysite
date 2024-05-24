from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *


class CommissionListView(ListView):
    model = Commission
    template_name = "commissions/commission_list.html"


class CommissionDetailView(LoginRequiredMixin, DetailView):
    model = Commission
    template_name = "commissions/commission_detail.html"
