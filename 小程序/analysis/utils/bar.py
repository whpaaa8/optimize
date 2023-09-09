from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.globals import ThemeType, RenderType
import meta

index = 0

# 绘制柱状图
# 柱状图  传入  x轴， y轴， 标题

def make_bar(keys, value_dict, title, reverse=False):
    global index
    index = index + 1
    pic = (
        Bar(
            # InitOpts 初始化配置项
            init_opts=opts.InitOpts(
                chart_id="bar_{}".format(index),
                width='550px',
                height='350px',  # 画布大小 css单位
                renderer=RenderType.CANVAS,  # 渲染风格， 可选 canvas，svg
                theme=meta.get_value("theme"),  # 主题
                # bg_color='white', # 背景颜色
            )
        )
        .add_xaxis(keys)
        # 全局配置项
        .set_global_opts(

            # TitleOpts: 标题配置项
            title_opts=opts.TitleOpts(
                title=title,  # 主标题
                # 标题位置
                pos_left='center',
                pos_top='2%',
                padding=10,  # 内边距
                item_gap=5,  # 主副标题间距
            ),

            # 区域缩放配置项
            #         datazoom_opts=opts.DataZoomOpts(
            #             is_show=True, # 显示区域缩放
            #             type_='inside', # 组件类型： slider 滑动条，inside（鼠标点击拖动缩放）
            #             is_realtime=True, # 拖动时实时更新
            #             range_start=20, # 数据窗口默认从%几开始
            #             range_end = 80, # 数据终止百分比
            #             orient='horizontal', # 滑动条位置 垂直vertical 水平
            #             is_zoom_lock=True, # 是否缩放锁定（平移时不能缩放）
            #         ),

            # 图例配置项
            legend_opts=opts.LegendOpts(
                # 图例类型：plain普通图例， scroll：可滚动图例（用于大量图例）
                type_='plain',
                is_show=True,  # 是否显示图例
                pos_right='0%',  # 图里位置：pos_left,right,top,bottom
                pos_top='10%',
                orient='vertical',  # 图例放置方式

                # 图例选择模式：点击事件
                # True：开启图例点击
                # False：关闭图例点击
                # single: 单选
                # multiple：多选
                selected_mode='multiple',

                # 图标和文字的位置
                align='left',
                # padding=20, # 内边距
                # item_gap=5, # 图例间的间距
                # item_width=30,
                # item_height=15,
                # inactive_color='#ccc', # 图例关闭时的颜色
                # PyEcharts常见图例图标： circle,rect,
                legend_icon='roundRect'
            ),

            # VisualMapOpts视觉映射配置项：配置值对应的颜色
            visualmap_opts=opts.VisualMapOpts(
                is_show=True,
                type_='color',  # color 或size
                min_=0,  # 最小值
                max_=100,
                range_opacity=0.7,  # 图片与文字透明度
                range_text=['max', 'min'],  # 最大最小值的文本
                #             range_color=['blue','green','blue'], # 渐变颜色
                orient='vertical',
                pos_bottom='7%',
                #             pos_right='5%',
                #             is_piecewise=True, # 是否分段显示
                #             is_inverse=True, # 是否翻转

            ),

            # AxisOpts: 坐标轴配置
            xaxis_opts=opts.AxisOpts(
                is_show=True,  # 是否显示x轴

                # 坐标轴类型：
                # value：数值轴， 用于连续数据
                # category： 类目轴，适用于离散数据
                # time： 时间轴，适用于连续时间，时序数据
                type_='category',
            ),

            yaxis_opts=opts.AxisOpts(

                # 不显示y轴的线
                axisline_opts=opts.AxisLineOpts(is_show=False),
                # 不显示刻度
                axistick_opts=opts.AxisTickOpts(is_show=False),
            ),
            toolbox_opts=opts.ToolboxOpts(
                pos_left="0",
                is_show=True,
                orient="horizontal",
                feature=opts.ToolBoxFeatureOpts(
                    save_as_image=opts.ToolBoxFeatureSaveAsImageOpts(type_="png", title="保存为png",
                                                                     pixel_ratio=2),
                    magic_type=opts.ToolBoxFeatureMagicTypeOpts(is_show=False),
                    data_zoom=opts.ToolBoxFeatureDataZoomOpts(is_show=False),
                    data_view=opts.ToolBoxFeatureDataViewOpts(is_show=False),
                    brush=opts.ToolBoxFeatureBrushOpts(type_="clear"),
                )
            ),
        ))

    for type1, values in value_dict.items():
        pic.add_yaxis(type1, values)
    if reverse:
        pic.reversal_axis()
    pic.set_series_opts(
        label_opts=opts.LabelOpts(is_show=False),
        markpoint_opts=opts.MarkPointOpts(
            data=[opts.MarkPointItem(type_='max', name='最大值'), opts.MarkPointItem(type_='min', name='最小值')]),
        markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_='average', name='平均值')]),
        minortick_opts=opts.MinorTickOpts(is_show=True)
    )
    return pic
