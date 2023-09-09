import pyecharts.options as opts
from pyecharts.charts import Gauge
from pyecharts.globals import RenderType, ThemeType

import meta

index = 0

# 绘制仪表盘
def make_gauge(rate, title):
    global index
    index = index + 1
    pic = Gauge(
        init_opts=opts.InitOpts(
            chart_id='gauge_{}'.format(index),
            width='550px',
            height='350px',  # 画布大小 css单位
            renderer=RenderType.CANVAS,  # 渲染风格， 可选 canvas，svg
            theme=meta.get_value("theme"),  # 主题
            # bg_color='white', # 背景颜色
        )).add(
        series_name=rate[0], data_pair=[rate],
        title_label_opts=opts.GaugeTitleOpts(offset_center=["0%", "30%"], color="red", font_weight="bold",
                                             font_size=20),
        detail_label_opts=opts.GaugeDetailOpts(formatter="{value}%", offset_center=["0%", "50%"], color='#33a3dc')
    ).set_global_opts(
        title_opts=opts.TitleOpts(title=title, pos_top='2%', pos_left="center"),
        legend_opts=opts.LegendOpts(is_show=False),
        tooltip_opts=opts.TooltipOpts(is_show=True, formatter="{a} <br/>{b} : {c}%"),
        toolbox_opts=opts.ToolboxOpts(
            is_show=True,
            pos_left="0",
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
    ).set_series_opts(
        axisline_opts=opts.AxisLineOpts(
            linestyle_opts=opts.LineStyleOpts(
                color=[[0.3, "#67e0e3"], [0.7, "#37a2da"], [1, "#fd666d"]], width=30
            )
        )
    )
    return pic
