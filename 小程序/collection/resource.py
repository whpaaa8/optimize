from import_export import resources
from .models import CollectionInfo
from import_export.fields import Field


# 导出的数据模型
class CollectionResource(resources.ModelResource):
    jobNumber = Field(attribute='jobNumber', column_name=CollectionInfo.jobNumber.field.verbose_name)
    associateNumber = Field(attribute='associateNumber', column_name=CollectionInfo.associateNumber.field.verbose_name)
    handler = Field(attribute='handler', column_name=CollectionInfo.handler.field.verbose_name)
    complaintType = Field(attribute='complaintType', column_name=CollectionInfo.complaintType.field.verbose_name)
    jobType = Field(attribute='jobType', column_name=CollectionInfo.jobType.field.verbose_name)
    date = Field(attribute='date', column_name=CollectionInfo.date.field.verbose_name)
    address = Field(attribute='address', column_name=CollectionInfo.address.field.verbose_name)

    lon = Field(attribute='lon', column_name=CollectionInfo.lon.field.verbose_name)
    lat = Field(attribute='lat', column_name=CollectionInfo.lat.field.verbose_name)

    # detailAddress = models.CharField(max_length=50, verbose_name="经纬度", blank=True)

    images_path = Field(attribute='images_path', column_name=CollectionInfo.images_path.field.verbose_name)
    # images = models.ImageField(upload_to=directory_path, verbose_name="相关图片", blank=True)

    testResult_path = Field(attribute='testResult_path', column_name=CollectionInfo.testResult_path.field.verbose_name)
    # testResult = models.ImageField(upload_to=directory_path, verbose_name="掌上优测试截图", blank=True)

    sign = Field(attribute='sign', column_name=CollectionInfo.sign.field.verbose_name)

    location = Field(attribute='location', column_name=CollectionInfo.location.field.verbose_name)
    # position = models.ImageField(upload_to=directory_path, verbose_name="问题定位图", blank=True)

    reason = Field(attribute='reason', column_name=CollectionInfo.reason.field.verbose_name)
    soluType = Field(attribute='soluType', column_name=CollectionInfo.soluType.field.verbose_name)

    testReport_path = Field(attribute='testReport_path', column_name=CollectionInfo.testReport_path.field.verbose_name)
    # testReport = models.FileField(upload_to=directory_path, blank=True, verbose_name="测试报告/测试需求")

    isSolve = Field(attribute='isSolve', column_name=CollectionInfo.isSolve.field.verbose_name)

    desc_path = Field(attribute='desc_path', column_name=CollectionInfo.desc_path.field.verbose_name)
    # desc = models.ImageField(upload_to=directory_path, verbose_name="解决截图说明", blank=True)

    remarks = Field(attribute='remarks', column_name=CollectionInfo.remarks.field.verbose_name)

    # 提交时间 自动
    submit_date = Field(attribute='submit_date', column_name=CollectionInfo.submit_date.field.verbose_name)
    # 提交者 自动
    submitter = Field(attribute='submitter', column_name=CollectionInfo.submitter.field.verbose_name)

    class Meta:
        model = CollectionInfo
