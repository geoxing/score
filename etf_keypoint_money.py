from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.faker import Faker
from pyecharts.commons.utils import JsCode
from datetime import datetime, timedelta
from pyecharts.globals import ThemeType
from lixinger_token import set_token
from lixinger_query import query_json
from tools import send_email_with_image, output_image
import yfinance as yf

def getCloseValues_overseas(etf_code):
    etf = yf.Ticker(etf_code)
    data = etf.history(period="1d")  # 获取当日分钟/小时数据
    if etf_code == "JPYCNY=X":
        return round(data["Close"].values[0]*100, 2) if not data.empty else None
    else:
        return round(data["Close"].values[0], 2) if not data.empty else None

def get_etf_keypoint_money():
    etf_info_map = {
        "518880.SS": {"name":"Gold","major_support":2.7,"minor_support":3.2,"minor_pressure":5.3,"major_pressure":6.2},
        "USDCNY=X": {"name":"USD","major_support":6.8,"minor_support":7.08,"minor_pressure":7.25,"major_pressure":7.37},
        "JPYCNY=X": {"name":"JPY","major_support":4.45,"minor_support":4.6,"minor_pressure":6,"major_pressure":6.7}
    }

    close_point_values={}

    # 获取当前日期和时间
    now = datetime.now()
    # 计算昨天的日期
    yesterday = now - timedelta(days=1)
    # 格式化当前日期为字符串
    formatted_date = now.strftime("%Y-%m-%d")
    print("当前日期 (格式化):", formatted_date)

    for item in etf_info_map.keys():
        result_close_point=getCloseValues_overseas(item)
        close_point_values[item]=result_close_point

    print(close_point_values)

    # 提取所有的 name 值
    etf_names = [info["name"] for info in etf_info_map.values()]

    # 创建一个新的字典来存储 major_support 作为键，major_support + 1 作为值
    major_supports = []
    minor_supports = []
    minor_pressures = []
    major_pressures = []
    close_points = []

    # 遍历原始字典并填充新的字典
    for stock_code, info in etf_info_map.items():
        major_support_value = info["major_support"]
        major_supports.append({"value":major_support_value,"showvalue":major_support_value})

        minor_support_value = info["minor_support"]
        minor_supports.append({"value":minor_support_value-major_support_value,"showvalue":minor_support_value})

        minor_pressure_value = info["minor_pressure"]
        minor_pressures.append({"value":minor_pressure_value-minor_support_value,"showvalue":minor_pressure_value})

        major_pressure_value = info["major_pressure"]
        major_pressures.append({"value":major_pressure_value-minor_pressure_value,"showvalue":major_pressure_value})

        close_point_value = close_point_values.get(stock_code)
        close_points.append({"value":close_point_value,"showvalue":close_point_value})

    print(major_supports)
    print(minor_supports)
    print(minor_pressures)
    print(major_pressures)
    print(close_points)

    # 创建Bar对象
    bar = (
        Bar(init_opts=opts.InitOpts(width="2400px", height="1600px", bg_color="white"))
        .add_xaxis(etf_names)
        .add_yaxis("major_support", major_supports, stack="stack1",bar_width="50%",gap="0%",itemstyle_opts=opts.ItemStyleOpts(color="#00da3c"))
        .add_yaxis("minor_support", minor_supports, stack="stack1",gap="0%",itemstyle_opts=opts.ItemStyleOpts(color="lightgreen"))
        .add_yaxis("minor_pressure", minor_pressures, stack="stack1",gap="0%",itemstyle_opts=opts.ItemStyleOpts(color="lightpink"))
        .add_yaxis("major_pressure", major_pressures, stack="stack1",gap="0%",itemstyle_opts=opts.ItemStyleOpts(color="#ec0000"))
        .add_yaxis("close_point", close_points,gap="0%",bar_width="20%",itemstyle_opts=opts.ItemStyleOpts(color="yellow"))
        .set_series_opts(
            label_opts=opts.LabelOpts(
                is_show=True,
                position="inside",
                formatter=JsCode(
                    "function(x){return Number(x.data.showvalue);}"
                ),
            )
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(is_show=False),
            legend_opts=opts.LegendOpts(is_show=False),
            tooltip_opts=opts.TooltipOpts(is_show=False)
        )
        .reversal_axis()
    )
    # 渲染图表到 HTML 文件
    output_html_file="etf_keypoint_money.html"
    bar.render("etf_keypoint_money.html")

    # 使用 snapshot-selenium 将 HTML 文件转换为图片
    output_image_file = "etf_keypoint_money.png"
    output_image(output_html_file,output_image_file)

    send_email_with_image("etf_keypoint_money","5908386@qq.com","5908386@qq.com","hakgazlgljxrbjbf","etf_keypoint_money.png","etf_keypoint_money")

# 检查当前模块是否是主程序
if __name__ == "__main__":
    get_etf_keypoint_money()
