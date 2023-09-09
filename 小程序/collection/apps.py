from django.apps import AppConfig


class CollectionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'collection'
    verbose_name = '运维工单收集表统计'