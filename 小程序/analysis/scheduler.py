from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
from .utils import main
import yaml
from .models import TimeModel
from datetime import datetime, timedelta

# 实例化调度器
scheduler = BackgroundScheduler()
# 调度器使用默认的DjangoJobStore()
scheduler.add_jobstore(DjangoJobStore(), 'default')


# 每个月1号5点半执行这个任务
@register_job(scheduler, 'cron', id='update', day=1, hour=5, minute=30)
def update():
    yesterday = datetime.today() - timedelta(days=1)  # 获取前一天的 datetime 对象
    yesterday_str = yesterday.strftime("%Y年%m月")  # 格式化为字符串
    with open("analysis/utils/config.yaml", "r", encoding='utf-8') as f:
        data = yaml.safe_load(f)  # 使用 safe_load 和 FullLoader
        print(data)
        data['time'] = yesterday_str
        print(data)
        print(data['time'])
    with open("analysis/utils/config.yaml", "w", encoding="utf-8") as f:
        print("write_data", data)
        yaml.dump(data, f)  # 使用 dump 和 RoundTripDumper
    main.get_page()
    TimeModel.objects.create(timestamp=yesterday, report_link="数据分析大屏_{}".format(yesterday_str))


def start_task():
    # 注册定时任务并开始
    register_events(scheduler)
    scheduler.start()
