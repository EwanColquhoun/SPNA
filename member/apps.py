from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ProfilesConfig(AppConfig):
    name = 'member'
    verbose_name = _('spnamembers')

    def ready(self):
        import member.signals
