def populate_models(sender, **kwargs):
    from django.apps import apps
    from .apps import OperationsConfig
    from django.contrib.auth.models import Group, Permission
    from django.contrib.contenttypes.models import ContentType

    group_settings, created = Group.objects.get_or_create(
        name=OperationsConfig.verbose_name)
    
    models = apps.all_models[OperationsConfig.name]
    for model in models:
        content_type = ContentType.objects.get(
            app_label=OperationsConfig.name,
            model=model
        )
        permissions = Permission.objects.filter(content_type=content_type)
        group_settings.permissions.add(*permissions)