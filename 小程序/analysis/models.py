from django.db import models


# Create your models here.
# 数据分析表模型“ 记录数据分析对应的时间以及文件名
class TimeModel(models.Model):
    timestamp = models.DateField(verbose_name="时间")
    report_link = models.CharField(verbose_name="数据分析结果", max_length=20, default="")

    def __str__(self):
        return self.report_link

    class Meta:
        verbose_name = "数据分析记录"