from django.contrib.auth.models import User
from django.db import models


class Ad(models.Model):
    def image_directory_path(self, filename) -> str:
        return "images/" + filename

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=100, null=False, blank=True)
    description = models.TextField(null=False, blank=True)
    image_url = models.ImageField(null=True, blank=True, upload_to=image_directory_path)
    category = models.CharField(max_length=50, null=False, blank=True)
    condition = models.CharField(max_length=50, null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class ExchangeProposal(models.Model):
    # Status Choices
    CHOICES = (
        ("ожидает", "expected"),
        ("принята", "accepted"),
        ("отклонена", "rejected"),
    )

    ad_sender = models.ForeignKey(Ad, related_name="sender", on_delete=models.PROTECT)
    ad_receiver = models.ForeignKey(Ad, related_name="receiver", on_delete=models.PROTECT)
    comment = models.CharField(max_length=100, null=False, blank=True)
    status = models.CharField(max_length=50, choices=CHOICES, default="ожидает")
    created_at = models.DateTimeField(auto_now_add=True)
