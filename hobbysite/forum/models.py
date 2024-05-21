from django.db import models
from django.urls import reverse


class PostCategory(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Post Categories"


class Post(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(
        "PostCategory", null=True, on_delete=models.SET_NULL, related_name="posts"
    )
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.title)

    def get_absolute_url(self):
        return reverse("forum:thread-detail", args=[self.pk])

    class Meta:
        ordering = ["-created_on"]
