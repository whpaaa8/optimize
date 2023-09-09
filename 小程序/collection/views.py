import os

from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import csv
import pandas as pd
from . import utils
from .forms import CollectionForm, CollectionTestFrom
from .models import CollectionInfo
from . import scheduler


def save_to_csv(data):
    filename = 'static/collection.csv'
    if not os.path.exists(filename):
        p = True
    else:
        p = False
    print(filename)
    values = data.values()
    fieldnames = ['id', '工单号', '关联工单号', '处理人', '投诉类型', '工单类型',
                  '处理时间', '投诉地址', '经度', '纬度', '相关图片', '掌上优测试截图',
                  '是否有联通信号', '问题定位图', '投诉原因', '方案类型', '测试报告/测试需求',
                  '是否解决', '解决截图说明', '备注', '提交时间', '提交人']
    data = dict(zip(fieldnames, values))
    # print(data)
    f = open(filename, 'a+', newline='')
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    if p: writer.writeheader()
    writer.writerow(data)


# 添加表单信息
@csrf_exempt
def add_collection(request):
    form = CollectionForm(request.POST, request.FILES)
    files_list = {'相关图片': request.FILES.getlist('images'), '掌上优测试截图': request.FILES.getlist('testResult'),
                  '问题定位图': request.FILES.getlist('position'), '已解决说明': request.FILES.getlist('desc'),
                  '测试报告或需求报告': request.FILES.getlist('testReport')}
    if form.is_valid():
        try:
            data = form.cleaned_data
            # 保存文件到本地
            paths = utils.upload_filelist(files_list, data)
            form.save(paths)
            return HttpResponse("success")
        except:
            return HttpResponse("Add Collection Error!")
    else:
        print(form.errors)
        return HttpResponse("failed")


# 查询表单信息
def collect_list(request):
    data = CollectionInfo.objects.all()
    print(data.values()[0].keys())
    data_list = serializers.serialize("json", data)
    return HttpResponse(data_list, content_type="application/json")


# 读数据
def write_collection(request):
    data = pd.read_excel("static/副本5月客服现场处理信息收集.xlsx")
    l = ['jobNumber', 'associateNumber', 'handler', 'complaintType',
         'jobType', 'date', 'address', 'lon', 'lat', 'images_path',
         'testResult_path', 'sign', 'location', 'reason', 'soluType',
         'testReport_path', 'isSolve', 'desc_path', 'remarks', 'submitter']

    models = []
    counts = 1
    for index, row in data.iterrows():
        if row['是否有联通信号（必填）'] == '有联通信号':
            row['是否有联通信号（必填）'] = 'True'
        else:
            row['是否有联通信号（必填）'] = 'False'

        if row['是否已解决/已闭环（必填）'] == '是':
            row['是否已解决/已闭环（必填）'] = 'True'
        else:
            row['是否已解决/已闭环（必填）'] = 'False'
        if row['工单号（必填）'] == '无' or row['工单号（必填）'] == '无工单号':
            row['工单号（必填）'] = '无工单号-' + str(counts)
            counts += 1
        if not pd.isnull(row['lon']):
            ll = row['lon'].split('，')
            row['lon'] = ll[0]
            row['lat'] = ll[1]
        # row.dropna(inplace=True)
        row.drop(['提交时间（自动）'], inplace=True)
        a = row.tolist()
        models.append(dict(zip(l, a)))
    print(len(models))
    for data1 in models:
        data1 = {k: v for k, v in data1.items() if not pd.isnull(v)}
        form = CollectionTestFrom(data1)
        # print(form.cleaned_data)
        # print(form)
        if form.is_valid():
            form.save()
        else:
            print(data1)
    return HttpResponse("success")


try:
    scheduler.start_task()
except:
    print("Task exists!")
def test_1(request):
    from datetime import date
    today = date.today()
    t = "2023\u5E7408\u6708"
    month = (today.month - 1) % 12 or 12
    print(month)
    month = 5
    qs = CollectionInfo.objects.filter(date__month=month)
    value_list = qs.values_list()
    data = pd.DataFrame(value_list)
    data.columns = (['id', '工单号', '关联工单号', '处理人', '投诉类型', '工单类型',
                  '处理时间', '投诉地址', '经度', '纬度', '相关图片', '掌上优测试截图',
                  '是否有联通信号', '问题定位图', '投诉原因', '方案类型', '测试报告/测试需求',
                  '是否解决', '解决截图说明', '备注', '提交时间', '提交人'])
    data['提交时间'] = data['提交时间'].apply(lambda x: x.tz_localize(None))
    data.to_excel("static/excel/处理工单收集表_{}.xlsx".format(t))
    return HttpResponse("yes")