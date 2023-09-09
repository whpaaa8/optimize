import json

import pandas as pd
import warnings

warnings.filterwarnings("ignore")
rate = 0
# 读取excel文件内容
data = []
date = 0
# 获取数据
def init(time):
    data1 = pd.read_excel("static/excel/处理工单收集表_{}.xlsx".format(time))
    global data, date
    data = data1
    date = time


# 获取工单类型 与闭环数据
def get_barData():
    data_type = data[['工单类型', '是否解决']]
    data_type['是否解决'] = data_type['是否解决'].replace({'TRUE': True, 'FALSE': False})
    data_type['工单类型'] = data_type['工单类型'].where(data_type['工单类型'].isin(
        ['政商助手', '抱怨单', '工信预处理', '通信保障']), '其他')

    #  各类型 工单数量
    value_counts = data_type['工单类型'].value_counts()
    # print(value_counts)
    # 各类型工单 闭环数量
    tmp = data_type.groupby('工单类型')['是否解决'].sum()
    global rate
    rate = '%.2f' % (data_type['是否解决'].sum() / data_type.shape[0] * 100)
    # 顺序
    order = pd.DataFrame(dict(order=[1, 2, 3, 4, 5]), index=['政商助手', '抱怨单', '工信预处理', '通信保障', '其他'])
    # 合并
    typeData = pd.concat([tmp, value_counts, order], axis=1)
    typeData.rename(columns={'工单类型': '数量', '是否解决': '已闭环数'}, inplace=True)
    # print(typeData)
    typeData['闭环率(%)'] = typeData.apply(lambda x: format(x['已闭环数'] / x['数量'] * 100, '.2f'), axis=1)
    typeData['闭环率(%)'] = typeData['闭环率(%)'].apply(lambda x: float(x))
    typeData.sort_values(by='order', inplace=True)

    typeData.dropna(axis=0, subset=['数量'], inplace=True)

    # 工单类型与闭环数量柱状图
    x = typeData.index.tolist()
    type_num = typeData['数量'].tolist()
    close_num = typeData['已闭环数'].tolist()
    close_rate = typeData['闭环率(%)'].tolist()
    y1 = {"工单数量": type_num, "已闭环数": close_num}
    y2 = {"闭环率": close_rate}
    return {'x': x, 'y1': y1, 'y2': y2}


# 获取闭环率
def get_rate():
    return tuple(["闭环率", rate])


# 获取饼图数据： 工单类型、投诉类型、工单投诉类型分布
def get_pieData():
    data_pie = data[['工单类型', '投诉类型', '投诉原因']]
    data_pie.rename(columns={'工单类型': '工单类型', '投诉类型': '投诉类型',
                             '投诉原因': '投诉原因'}, inplace=True)
    data_pie['工单类型'] = data_pie['工单类型'].where(data_pie['工单类型'].isin(
        ['政商助手', '抱怨单', '工信预处理', '通信保障']), '其他')
    data_pie['投诉类型'] = data_pie['投诉类型'].where(data_pie['投诉类型'].isin(
        ['4G', '5G', 'VOLTE', 'VONR', 'NB']), '其他')
    data_pie['投诉原因'] = data_pie['投诉原因'].where(data_pie['投诉原因'].isin(
        ['2G投诉', '弱覆盖', '非网络侧-其他', '干扰', '故障', '基站过忙', '用户终端机卡', '直放站性能问题',
         '切换问题']), '其他')
    Data1 = data_pie['工单类型'].value_counts()
    dict1 = [Data1.index.tolist(), Data1.values.tolist()]
    Data2 = data_pie['投诉类型'].value_counts()
    dict2 = [Data2.index.tolist(), Data2.values.tolist()]
    Data3 = data_pie['投诉原因'].value_counts()
    dict3 = [Data3.index.tolist(), Data3.values.tolist()]
    return {'工单类型': dict1, '投诉类型': dict2, '投诉原因': dict3}


# 获取折线图 时间序列
def get_lineData():
    data_line = data[['提交时间（自动）']]
    data_line['number'] = 1
    data_line.rename(columns={'提交时间（自动）': '时间'}, inplace=True)
    data_line.set_index("时间", inplace=True)
    tmp = data_line['number'].resample('1D').count()
    tmp = tmp.loc[tmp.index.dayofweek < 5]
    keys = tmp.index.strftime('%m-%d').tolist()
    values = {"投诉工单数": tmp.values.tolist()}
    return [keys, values]


def get_mapData():
    # data1 = pd.read_excel("投诉工单.xlsx")[['Address', 'Longitude', 'Latitude', '受理日期']]
    data1 = data[['投诉地址', '经度', '纬度', '处理时间']]
    data1['投诉地址'] = data1['投诉地址'].apply(lambda x: x[x.rfind('/')+1:])
    # 坐标json
    site = {}
    points = []
    filename = "site_{}.json".format(date)
    for index, row in data1.iterrows():
        site[row[0]] = [row[1], row[2]]
        tmp = [row[0], row[3]]
        points.append(tmp)

    with open(filename, 'w') as f:
        json.dump(site, f)

    return filename, points

# typeData = get_typeData()
# print(typeData)
# print(rate)
# print(get_rate())
# print(get_pieData())
