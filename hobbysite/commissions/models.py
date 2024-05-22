from django.db import models
from django.urls import reverse


class Commission(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    required_ppl = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.title)

    def get_absolute_url(self):
        return reverse("commissions:comm-detail", args=[self.pk])

    class Meta:
        ordering = ["created_on"]


class Comment(models.Model):
    commission = models.ForeignKey(
        "Commission", null=True, on_delete=models.CASCADE, related_name="commissions"
    )
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]
