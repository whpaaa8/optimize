from pyecharts.commons.utils import JsCode
from pyecharts.charts import BMap
from pyecharts.globals import BMapType, ChartType, RenderType, ThemeType
from pyecharts import options as opts


# 地图 site：json 地点经纬度json ;data：数据名称和值; ak:百度地图 key
def make_map(site, data, ak):
    mp = (BMap(init_opts=opts.InitOpts(
        chart_id='chart_mp1',
        width='1650px',
        height='800px',  # 画布大小 css单位
        renderer=RenderType.CANVAS,  # 渲染风格， 可选 canvas，svg
        # theme=ThemeType.DARK,  # 主题
        # bg_color='white', # 背景颜色
    ), is_ignore_nonexistent_coord=True
    ).add_coordinate_json(site).add_schema(
        # 百度地图 key
        baidu_ak=ak,
        center=[113.38, 22.52],
        zoom=13,
        is_roam=True,
    ).add(
        series_name="投诉地点",
        type_="effectScatter",
        data_pair=data,
        symbol_size=11,
        is_polyline=True,
        is_large=True,
        effect_opts=opts.EffectOpts(period=6),
        label_opts=opts.LabelOpts(position="right", is_show=False),
        itemstyle_opts=opts.ItemStyleOpts(color="red"),
        tooltip_opts=opts.TooltipOpts(trigger="item", formatter=JsCode(
            # 回调函数的参数是一个对象，包含数据点的坐标和其他属性
            "function (params) {"
            # 使用return语句返回一个字符串作为提示框的内容
            # 可以使用params.data[0]和params.data[1]访问数据点的经纬度
            # 可以使用params.data[2]访问数据点的其他属性，比如大小
            "console.log(params.data.value);"
            "return '<strong style=color:yellow>'+params.name +'</strong>'+ '<br/>'+params.marker +'经度: ' + "
            "params.value[0] + '<br/>'+ params.marker +'纬度: ' + params.value[1]+'<br/>'+ params.marker +'时间: ' + "
            "params.value[2];"
            "}")
                                      ),
    ).add_control_panel(
        maptype_control_opts=opts.BMapTypeControlOpts(
            type_=BMapType.MAPTYPE_CONTROL_DROPDOWN
        ),
        scale_control_opts=opts.BMapScaleControlOpts(),
        overview_map_opts=opts.BMapOverviewMapControlOpts(is_open=True),
        navigation_control_opts=opts.BMapNavigationControlOpts(position=0),
        geo_location_control_opts=opts.BMapGeoLocationControlOpts(),
    ).set_global_opts(
        legend_opts=opts.LegendOpts(orient="vertical",
                                    textstyle_opts=opts.TextStyleOpts(font_size=20, font_weight='bold'),
                                    background_color='yellow', pos_top="3%"),))
    mp.add_js_funcs(
        """
       chart_chart_mp1.on("click", function (params) {
            if (params.componentType === "series") {
                var coord = [params.value[0],params.value[1]];
                chart_chart_mp1.setOption({
                    bmap: {
                        center: coord,
                        zoom: 18
                    }
                });
            }
            return 
        });""")


    return mp
