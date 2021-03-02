from rest_framework import serializers

from ..models import Card


class CardDetailSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Card
        fields = "__all__"
