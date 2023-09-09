from pyecharts.charts import Page
from pyecharts.components import Table
from . import get_data
from . import meta
from .bar import make_bar
from .pie import make_Pie, make_Rose_Pie, make_Simple_Pie
from .gauge import make_gauge
from .line import make_Line
from .map import make_map
from pyecharts.globals import CurrentConfig, ThemeType
from pyecharts import options as opts
CurrentConfig.ONLINE_HOST = "/static/pyecharts-assets-master/assets/"

# 主程序，用于获取数据大屏
def get_page():
    meta._init()

    # 设置数据月份
    month = meta.get_value('month')
    # 获取ak
    map_ak = meta.get_value('ak')
    table_color = ""
    # 设置主题颜色

    theme_color = meta.get_value("theme")  # 主题
    if theme_color == ThemeType.DARK:
        table_color = '#333333'
    elif theme_color == ThemeType.CHALK:
        table_color = '#293441'
    elif theme_color == ThemeType.PURPLE_PASSION:
        table_color = '#5B5C6E'
    elif theme_color == ThemeType.ROMANTIC:
        table_color = '#F0E8CD'
    elif theme_color == ThemeType.ESSOS:
        table_color = '#FDFCF5'
    else:
        table_color = ''

    index = 0


    def make_title(title, height="50px", fontsize="50px", color="#C0C0C0"):
        global index
        index += 1
        """ 制作大标题 """
        table = Table()
        table.chart_id = "table_{}".format(index)
        global table_color
        table.add(headers=[title], rows=[], attributes={
            "align": "center",
            "border": False,
            "padding": "10px",
            "style": "background:{}; width:1650px; height:{};font-size:{};color:{};".format(table_color,
                                                                                            height, fontsize, color)
        })
        table.render('大标题.html')
        # print('生成完毕： 大标题')
        return table


    page = Page(
        page_title="整合数据分析大屏",
        layout=Page.DraggablePageLayout,
    )
    # 获取所有数据
    get_data.init(month)
    # 第一二个柱状图数据： 工单类型、闭环数
    Bar_data = get_data.get_barData()
    # 获取饼图数据
    Pie_data = get_data.get_pieData()
    # 获取仪表盘数据
    Gauge_data = get_data.get_rate()
    # 获取折线图数据
    Line_data = get_data.get_lineData()
    # 获取地图数据
    Map_data = get_data.get_mapData()

    page.add(
        # 增加 屏幕 大标题
        make_title(title="客服投诉工单数据分析大屏"),

        # 绘制柱状图1： 工单类型与闭环数
        make_bar(Bar_data['x'], Bar_data['y1'], title="{}投诉工单与闭环数量".format(month)),

        # 绘制柱状图2： 工单类型与闭环率
        make_bar(Bar_data['x'], Bar_data['y2'], title="{}投诉工单闭环率".format(month)),
        # 绘制饼图1： 工单类型
        # make_Pie(Pie_data['工单类型'][0], Pie_data['工单类型'][1], title="{}投诉工单类型分布".format(month)),

        # 绘制饼图2: 投诉类型
        make_Simple_Pie(Pie_data['投诉类型'][0], Pie_data['投诉类型'][1], title="{}工单投诉类型分布".format(month)),
        # make_Rose_Pie(Pie_data['投诉类型'][0], Pie_data['投诉类型'][1], title="{}工单投诉类型分布".format(month)),

        # 绘制饼图3： 投诉原因
        # make_Simple_Pie(Pie_data['投诉原因'][0], Pie_data['投诉原因'][1], title="{}工单投诉原因分布".format(month)),
        make_Rose_Pie(Pie_data['投诉原因'][0], Pie_data['投诉原因'][1], title="{}工单投诉原因分布".format(month)),

        # 绘制仪表盘： 整体闭环率
        make_gauge(Gauge_data, title="{}工单闭环率".format(month)),

        # 绘制折线图： 每天的投诉量
        make_Line(Line_data[0], Line_data[1], title="{}投诉工单分布".format(month)),

        # 绘制地图标题: 投诉点地理位置分布
        make_title("投诉点地理位置分布", height="20px", fontsize="20px"),

        # 绘制地图： 投诉地点分布
        make_map(Map_data[0], Map_data[1], ak=map_ak),

    ).add_js_funcs('''
        // 获取 BMap 对象，以便监听 tilesloaded 事件
        var bmap = chart_chart_mp1.getModel().getComponent('bmap').getBMap();
        
        // 监听 tilesloaded 事件，在地图加载完成后执行操作
        bmap.addEventListener('tilesloaded', function () {
             chart_chart_mp1.click(); // 重新调整图表大小
        });
    ''')
    page.render("临时大屏_{}.html".format(month))
    Page.save_resize_html(
        source="临时大屏_{}.html".format(month),
        cfg_file="config.json",
        dest="templates/数据分析大屏_{}.html".format(month),
    )