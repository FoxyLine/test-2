from rest_framework import serializers

from ..models import Card


class CardDetailSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    order = serializers.PrimaryKeyRelatedField(read_only=True) # for
    

    class Meta:
        model = Card
        fields = "__all__"
