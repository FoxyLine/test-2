from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CardsConfig(AppConfig):
    name = "kanban.cards"
    verbose_name = _("Kanban Cards")
