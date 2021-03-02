from django.contrib import admin
from .models import Card

@admin.register(Card)
class CardAmin(admin.ModelAdmin):
    class Meta:
        model = Card