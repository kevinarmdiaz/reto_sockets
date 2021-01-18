from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DevicesConfig(AppConfig):
    name = "device_backend.devices"
    verbose_name = _("Devices")

    def ready(self):
        try:
            import device_backend.devices.signals  # noqa F401
        except ImportError:
            print("No importado")
            pass
