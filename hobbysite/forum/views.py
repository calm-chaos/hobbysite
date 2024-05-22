from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *


class ForumListView(ListView):
    model = Post
    template_name = "forum_list.html"


class ForumDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "forum_detail.html"
