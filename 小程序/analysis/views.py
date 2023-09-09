from django.shortcuts import render
from . import scheduler
from django.conf import settings

# Create your views here.

# 开启自动分析
try:
    scheduler.start_task()
except:
    print("Task exists!")


def show(request, report_link):
    template_name = f'{report_link}.html'
    print(template_name)
    return render(request, template_name)
