from import_export import resources
from .models import UserInfo
from import_export.fields import Field


class UserResource(resources.ModelResource):
    uname = Field(attribute='uname', column_name=UserInfo.uname.field.verbose_name)

    class Meta:
        model = UserInfo
