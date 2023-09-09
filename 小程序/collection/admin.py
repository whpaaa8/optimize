from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import CollectionInfo
from .resource import CollectionResource


# Register your models here.
class CollectionInfoAdmin(ImportExportModelAdmin):
    resource_class = CollectionResource
    list_display = ['jobNumber', 'jobType', 'handler', 'submitter']
    search_fields = ['jobNumber', 'jobType', 'handler', 'associateNumber', 'address']
    date_hierarchy = 'date'


admin.site.register(CollectionInfo, CollectionInfoAdmin)
