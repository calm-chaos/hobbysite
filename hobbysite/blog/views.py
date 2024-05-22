from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *


class BlogListView(ListView):
    model = Article
    template_name = "blog_list.html"


class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = "blog_detail.html"
