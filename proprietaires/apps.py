from django.apps import AppConfig
from django.db.models.signals import post_migrate


class ProprietairesConfig(AppConfig):
    name = 'proprietaires'
    verbose_name = 'Gestion des Proprietaires'

    def ready(self):
        from .signals import populate_models
        post_migrate.connect(populate_models, sender=self)