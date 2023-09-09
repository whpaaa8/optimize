from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import UserInfo
from .resource import UserResource


# Register your models here.

# 注册到后台


class UserInfoAdmin(ImportExportModelAdmin):
    resource_class = UserResource
    list_display = ['username', 'uname']
    search_fields = ['username', 'uname']


admin.site.register(UserInfo, UserInfoAdmin)
