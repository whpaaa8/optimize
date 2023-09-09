from pyecharts.globals import CurrentConfig, ThemeType
import yaml
# 读取配置文件，全局数据
t = {'DARK': ThemeType.DARK, 'PURPLE_PASSION': ThemeType.PURPLE_PASSION, 'CHALK': ThemeType.CHALK,
     'ROMANTIC': ThemeType.ROMANTIC, 'ESSOS': ThemeType.ESSOS}


def _init():  # 初始化
    with open('config.yaml', 'rb') as f:
        content = f.read()
        data = yaml.load(content, Loader=yaml.FullLoader)
    global _global_dict
    _global_dict = {'theme': t[data['themeType']], 'month': data['time'], 'ak': data['ak']}


def set_value(key, value):
    # 定义一个全局变量
    _global_dict[key] = value


def get_value(key):
    # 获得一个全局变量，不存在则提示读取对应变量失败
    try:
        return _global_dict[key]
    except:
        print('读取' + key + '失败\r\n')

