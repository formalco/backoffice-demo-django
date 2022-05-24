from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PiiConfig(AppConfig):
    name = "backoffice_demo_django.pii"
    verbose_name = _("Pii")

    def ready(self):
        try:
            import backoffice_demo_django.pii.signals  # noqa F401
        except ImportError:
            pass
