from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "backoffice_demo_django.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import backoffice_demo_django.users.signals  # noqa F401
        except ImportError:
            pass
