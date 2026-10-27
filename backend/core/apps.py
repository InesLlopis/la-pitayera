# UD3.2.f
from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
    # UD3.4.d
    verbose_name = "Core"
