def populate_models(sender, **kwargs):
    from django.apps import apps
    from .apps import SettingsConfig
    from django.contrib.auth.models import Group, Permission
    from django.contrib.contenttypes.models import ContentType

    group_settings, created = Group.objects.get_or_create(
        name=SettingsConfig.verbose_name)
    
    models = apps.all_models[SettingsConfig.name]
    for model in models:
        content_type = ContentType.objects.get(
            app_label=SettingsConfig.name,
            model=model
        )
        permissions = Permission.objects.filter(content_type=content_type)
        group_settings.permissions.add(*permissions)