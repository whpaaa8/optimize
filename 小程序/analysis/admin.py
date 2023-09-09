from django.contrib import admin
from django.utils.html import format_html
from .models import TimeModel
from django.urls import reverse



class TimeModelAdmin(admin.ModelAdmin):
    list_display = ('formatted_timestamp', 'display_report_link')
    # list_filter = ('timestamp',)  # 可选，根据需要添加过滤器
    search_fields = ['formatted_timestamp']
    date_hierarchy = 'timestamp'

    def display_report_link(self, obj):
        if obj.report_link:
            url = reverse('analysis_template', args=[obj.report_link])
            return format_html('<a href="{}" target="_blank">查看报告</a>', url)
        else:
            return "无报告链接"

    def formatted_timestamp(self, obj):
        return obj.timestamp.strftime('%Y年%m月') if obj.timestamp else ''

    formatted_timestamp.short_description = '时间'
    display_report_link.short_description = '数据分析报告'


admin.site.register(TimeModel, TimeModelAdmin)
