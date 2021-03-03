from django.db import models
from django.db.models import F


from django.contrib.auth import get_user_model

from django.utils import timezone
from .fields import OrderField

User = get_user_model()


class Card(models.Model):
    TYPE_CARDS = (
        ("RED", "ON_HOLD"),
        ("BLUE", "IN_PROGRESS"),
        ("YELLOW", "NEED_REVIEW"),
        ("GREEN", "APPROVED"),
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=8, choices=TYPE_CARDS)
    text = models.TextField()

    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    order = OrderField(blank=True, for_fields=["type"])

    def set_order(self, order):
        lower_order = Card.objects.filter(order__gte=order, type=self.type)

        if lower_order.filter(order=order).exists():
            lower_order.update(order=F("order") + 1)

        self.order = order
        self.save(update_fields=["order"])

    def change_type(self, type):
        self.type = type
        self.save()

    def __str__(self):
        return f"{self.user.username}:{self.type}:{self.text}"

    class Meta:
        ordering = ["order"]
