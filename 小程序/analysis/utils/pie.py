from pyecharts.charts import Pie
from pyecharts import options as opts
from pyecharts.globals import ThemeType, RenderType

import meta

index = 0


# 饼图
def make_Pie(keys, values, title):
    global index
    index = index + 1
    post_type = (
        Pie(init_opts=opts.InitOpts(
            chart_id='pie_{}'.format(index),
            width='550px',
            height='350px',  # 画布大小 css单位
            renderer=RenderType.CANVAS,  # 渲染风格， 可选 canvas，svg
            theme=meta.get_value("theme"),  # 主题
            # bg_color='white', # 背景颜色
        ))
        .add(
            "工单",
            [list(z) for z in zip(keys, values)],
            radius=["40%", "75%"],
        )
        .set_global_opts(title_opts=opts.TitleOpts(title=title, pos_top='2%', pos_left='center'),
                         legend_opts=opts.LegendOpts(orient="vertical", pos_right="0%"),
                         tooltip_opts=opts.TooltipOpts(
                             trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
                         ),
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
                         ).set_series_opts(label_opts=opts.LabelOpts(formatter="{b} "))
    )
    return post_type


# 简易饼图
def make_Simple_Pie(keys, values, title):
    global index
    index = index + 1
    pic = Pie(init_opts=opts.InitOpts(
        chart_id='pie_{}'.format(index),
        width='550px',
        height='350px',  # 画布大小 css单位
        renderer=RenderType.CANVAS,  # 渲染风格， 可选 canvas，svg
        theme=meta.get_value("theme"),  # 主题
        # bg_color='white', # 背景颜色
    )).add(
        series_name=title,
        data_pair=[list(z) for z in zip(keys, values)],
        radius=["50%", "70%"],
        label_opts=opts.LabelOpts(is_show=True, position="left"),
    ).set_global_opts(title_opts=opts.TitleOpts(title=title, pos_top='2%', pos_left="center"),
                      legend_opts=opts.LegendOpts(pos_right="0", orient="vertical"),
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
                      )).set_series_opts(
        tooltip_opts=opts.TooltipOpts(
            trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
        ),
        # label_opts=opts.LabelOpts(formatter="{b}: {c}")
    )
    return pic


# 玫瑰图
def make_Rose_Pie(keys, values, title):
    global index
    index = index + 1
    pic = Pie(init_opts=opts.InitOpts(
        chart_id='pie_{}'.format(index),
        width='550px',
        height='350px',  # 画布大小 css单位
        renderer=RenderType.CANVAS,  # 渲染风格， 可选 canvas，svg
        theme=meta.get_value("theme"),  # 主题
        # bg_color='white', # 背景颜色
    )).add(
        "",
        [list(z) for z in zip(keys, values)],
        radius=["30%", "75%"],
        # center=["75%", "50%"],
        rosetype="area",
    ).set_global_opts(title_opts=opts.TitleOpts(title=title, pos_top='2%', pos_left='center'),
                      legend_opts=opts.LegendOpts(orient="vertical", pos_right="0%"),
                      tooltip_opts=opts.TooltipOpts(
                          trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
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
                      ).set_series_opts(label_opts=opts.LabelOpts(formatter="{b} "))
    return pic
