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
    return round(data["Close"].values[0], 2) if not data.empty else None

def get_etf_keypoint_overseas():
    etf_info_map = {
        "^HSI": {"name":"HK","major_support":14863,"minor_support":18415,"minor_pressure":25000,"major_pressure":33000},
        # "H30533.SS": {"name":"ZhongGai","major_support":3415,"minor_support":5122,"minor_pressure":8000,"major_pressure":17000},
        # "H11136": {"name":"CNHuLian","major_support":2500,"minor_support":3739,"minor_pressure":7500,"major_pressure":12463},
        # "HSTECH": {"name":"HKKeJi","major_support":2200,"minor_support":3300,"minor_pressure":7600,"major_pressure":10000},
        # "HSHCI": {"name":"HKYiLiao","major_support":2168,"minor_support":2340,"minor_pressure":2900,"major_pressure":4300},
        # "00700": {"name":"Tencent","major_support":140,"minor_support":290,"minor_pressure":420,"major_pressure":700},
        "^GDAXI": {"name":"Dax","major_support":8200,"minor_support":11000,"minor_pressure":15000,"major_pressure":20000},
        "^SPX": {"name":"BP500","major_support":2000,"minor_support":2300,"minor_pressure":5254,"major_pressure":6000},
        "^IXIC": {"name":"NSDK","major_support":4800,"minor_support":6800,"minor_pressure":16000,"major_pressure":20000},
        "^NDX": {"name":"NSDK100","major_support":4200,"minor_support":7000,"minor_pressure":18000,"major_pressure":21000},
        # "518880": {"name":"Gold","major_support":2.7,"minor_support":3.2,"minor_pressure":5.3,"major_pressure":6.2},
        # "USDCNH": {"name":"USD","major_support":6.8,"minor_support":7.08,"minor_pressure":7.25,"major_pressure":7.37},
        # "JPYCNY": {"name":"JPY","major_support":4.45,"minor_support":4.6,"minor_pressure":6,"major_pressure":6.7}
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
    output_html_file="etf_keypoint_overseas.html"
    bar.render("etf_keypoint_overseas.html")

    # 使用 snapshot-selenium 将 HTML 文件转换为图片
    output_image_file = "etf_keypoint_overseas.png"
    output_image(output_html_file,output_image_file)

    send_email_with_image("etf_keypoint_overseas","5908386@qq.com","5908386@qq.com","hakgazlgljxrbjbf","etf_keypoint_overseas.png","etf_keypoint_overseas")

# 检查当前模块是否是主程序
if __name__ == "__main__":
    get_etf_keypoint_overseas()
