import random
from pyecharts.charts import Line
from pyecharts import options as opts
from pyecharts.globals import ThemeType, RenderType
from pyecharts.faker import Faker

import meta

index = 0

# 线型图
def make_Line(keys, values, title):
    i = 0
    global index
    index = index + 1
    pic = Line(
        init_opts=opts.InitOpts(
            chart_id='line_{}'.format(index),
            width='550px',
            height='350px',  # 画布大小 css单位
            renderer=RenderType.CANVAS,  # 渲染风格， 可选 canvas，svg
            theme=meta.get_value("theme"),  # 主题
            # bg_color='white', # 背景颜色
        )
    ).add_xaxis(keys)
    for name, value in values.items():
        pic.add_yaxis(
            series_name=name,
            is_smooth=True,
            color=Faker.rand_color(),
            y_axis=value,
            linestyle_opts=opts.LineStyleOpts(width=3),
            markpoint_opts=opts.MarkPointOpts(
                data=[
                    opts.MarkPointItem(type_="max", name="最大值"),
                    opts.MarkPointItem(type_="min", name="最小值"),
                ]
            ),
            markline_opts=opts.MarkLineOpts(
                data=[opts.MarkLineItem(type_="average", name="平均值")]
            ),
        )
        i += 1
    pic.set_global_opts(
        title_opts=opts.TitleOpts(title=title, pos_top='2%', pos_left="center"),
        legend_opts=opts.LegendOpts(orient="vertical", pos_right="0%", pos_top="5%"),
        tooltip_opts=opts.TooltipOpts(trigger="axis"),
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
        xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
    )
    return pic
