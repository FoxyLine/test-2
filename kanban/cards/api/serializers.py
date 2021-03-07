from rest_framework import serializers

from ..models import Card


class FormatedDateTime(serializers.DateTimeField):
    def to_representation(self, value):
        date = value.strftime("%Y-%m-%d %H:%M")
        return date

class CardDetailSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    order = serializers.IntegerField(required=False)
    create_date = FormatedDateTime(read_only=True)
    update_date = FormatedDateTime(read_only=True)

    def validate_order(self, order):
        if order < 0:
            raise serializers.ValidationError("Order must be positive")
        return order

    def validate_type(self, type):
        types = [Card.RED, Card.BLUE, Card.YELLOW, Card.GREEN]

        if type not in types:
            raise serializers.ValidationError(
                "The type must be one of {types}".format(types=", ".join(types))
            )

        return type

    class Meta:
        model = Card
        fields = "__all__"
