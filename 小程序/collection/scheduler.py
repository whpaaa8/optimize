import pandas as pd
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
from .models import CollectionInfo

def get_time():
    from datetime import datetime, timedelta
    yesterday = datetime.today() - timedelta(days=1)  # 获取前一天的 datetime 对象
    yesterday_str = yesterday.strftime("%Y年%m月")  # 格式化为字符串
    return yesterday_str

# 实例化调度器
scheduler = BackgroundScheduler()
# 调度器使用默认的DjangoJobStore()
scheduler.add_jobstore(DjangoJobStore(), 'default')

# 每个月1号2点半执行这个任务
@register_job(scheduler, 'cron', id='update_data_to_excel', day=1, hour=2, minute=30)
def update_data():
    from datetime import date
    today = date.today()
    month = (today.month - 1) % 12 or 12
    qs = CollectionInfo.objects.filter(date__month=month)
    value_list = qs.values_list()
    data = pd.DataFrame(value_list)
    data.columns = (['id', '工单号', '关联工单号', '处理人', '投诉类型', '工单类型',
                     '处理时间', '投诉地址', '经度', '纬度', '相关图片', '掌上优测试截图',
                     '是否有联通信号', '问题定位图', '投诉原因', '方案类型', '测试报告/测试需求',
                     '是否解决', '解决截图说明', '备注', '提交时间', '提交人'])
    data['提交时间'] = data['提交时间'].apply(lambda x: x.tz_localize(None))
    data.to_excel("static/excel/处理工单收集表_{}.xlsx".format(get_time()))

def start_task():
    # 注册定时任务并开始
    register_events(scheduler)
    scheduler.start()
