import os

from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
import uuid
import shutil

from django.conf import settings
from django.utils import timezone


# Create your models here.

#  这个函数应该是无用的，之前用到过，但可能经过makemigrations，注释掉会报错，实际运行不影响
def directory_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex[:10], ext)
    sub_folder = 'file'
    if ext.lower() in ["jpg", "png", "gif"]:
        sub_folder = "avatar"
    if ext.lower() in ["pdf", "docx", "doc"]:
        sub_folder = "document"
    # return the whole path to the file
    return os.path.join(instance.jobNumber, sub_folder, filename)


# 收集表表单模型
class CollectionInfo(models.Model):
    jobNumber = models.CharField(max_length=30, verbose_name="工单号", unique=True)
    associateNumber = models.CharField(max_length=50, verbose_name="收集表工单号")
    handler = models.CharField(max_length=30, verbose_name="处理人")
    TYPE_CHOICES = [
        ('4G', '4G'),
        ('5G', '5G'),
        ('VOLTE', 'VOLTE'),
        ('VONR', 'VONR'),
        ('NB', 'NB'),
    ]
    complaintType = models.CharField(max_length=50, verbose_name="投诉类型", choices=TYPE_CHOICES)
    jobType = models.CharField(max_length=50, verbose_name="工单类型")
    date = models.DateField(verbose_name="处理时间")
    address = models.CharField(max_length=50, verbose_name="投诉地址")

    lon = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="经度", blank=True, null=True)
    lat = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="纬度", blank=True, null=True)


    images_path = models.CharField(max_length=1000, verbose_name="相关图片", blank=True, null=True)
    # images = models.ImageField(upload_to=directory_path, verbose_name="相关图片", blank=True)

    testResult_path = models.CharField(max_length=1000, verbose_name="掌上优测试截图", blank=True, null=True)
    # testResult = models.ImageField(upload_to=directory_path, verbose_name="掌上优测试截图", blank=True)

    sign = models.BooleanField(verbose_name="是否有联通信号")

    location = models.CharField(max_length=1000, verbose_name="问题定位图", blank=True, null=True)
    # position = models.ImageField(upload_to=directory_path, verbose_name="问题定位图", blank=True)

    reason = models.CharField(max_length=50, verbose_name="投诉原因")
    soluType = models.CharField(max_length=150, verbose_name="方案类型")

    testReport_path = models.CharField(max_length=1000, verbose_name="测试报告/测试需求", blank=True, null=True)
    # testReport = models.FileField(upload_to=directory_path, blank=True, verbose_name="测试报告/测试需求")

    isSolve = models.BooleanField(verbose_name="是否解决")

    desc_path = models.CharField(max_length=1000, verbose_name="解决截图说明", blank=True, null=True)
    # desc = models.ImageField(upload_to=directory_path, verbose_name="解决截图说明", blank=True)

    remarks = models.CharField(max_length=1000, verbose_name="备注", blank=True, null=True)

    # 提交时间 自动
    submit_date = models.DateTimeField(default=timezone.now, verbose_name="提交时间")
    # 提交者 自动
    submitter = models.CharField(max_length=1000, verbose_name="提交者", default="暂无")

    class Meta:
        verbose_name = "客服现场处理信息收集表"

    def __str__(self):
        return self.associateNumber


# 删除记录时，同时删除本地数据
@receiver(post_delete, sender=CollectionInfo)
def delete_upload_files(sender, instance, **kwargs):
    directory = os.path.join(settings.MEDIA_ROOT, instance.jobNumber)
    if os.path.exists(directory):
        shutil.rmtree(directory)
    else:
        print(directory)
