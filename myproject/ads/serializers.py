from rest_framework import serializers

from .models import Ad, ExchangeProposal


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = (
            "pk",
            "title",
            "description",
            "user",
            "category",
            "condition",
            "created_at",
            "image_url",
        )


class ExchangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangeProposal
        fields = (
            "pk",
            "ad_sender",
            "ad_receiver",
            "comment",
            "status",
            "created_at",
        )
