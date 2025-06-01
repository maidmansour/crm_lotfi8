def populate_models(sender, **kwargs):
    from django.apps import apps
    from .apps import ProprietairesConfig
    from django.contrib.auth.models import Group, Permission
    from django.contrib.contenttypes.models import ContentType

    group_settings, created = Group.objects.get_or_create(
        name=ProprietairesConfig.verbose_name)
    
    models = apps.all_models[ProprietairesConfig.name]
    for model in models:
        content_type = ContentType.objects.get(
            app_label=ProprietairesConfig.name,
            model=model
        )
        permissions = Permission.objects.filter(content_type=content_type)
        group_settings.permissions.add(*permissions)