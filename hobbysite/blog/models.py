from django.db import models
from django.urls import reverse


class ArticleCategory(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Article Categories"


class Article(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(
        "ArticleCategory", null=True, on_delete=models.SET_NULL, related_name="articles"
    )
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.title)

    def get_absolute_url(self):
        return reverse("blog:article-detail", args=[self.pk])

    class Meta:
        ordering = ["-created_on"]
