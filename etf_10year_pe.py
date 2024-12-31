import json
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from pyecharts import options as opts
from pyecharts.charts import Line
from pyecharts.globals import ThemeType
from lixinger_token import set_token
from lixinger_query import query_json
from tools import output_image, send_email_with_image


#基本面数据API
#https://open.lixinger.com/api/cn/index/fundamental
# json_rltk = lo.query_json('cn/index/fundamental', {
#     "startDate": "2023-12-03",
#     "endDate": "2024-12-03",
#     "stockCodes": ["000001","000905"],
#     "metricsList": [
#         "pe_ttm.mcw"
#     ]
# })
# print(json_rltk)

def getPEValues(stockCode="000001"):
    # 获取当前日期
    today = datetime.today()
    # 计算十年前的日期（简单计算）
    ten_years_ago_simple = today - timedelta(days=10 * 365)

    # 计算十年前的日期（精确计算）
    ten_years_ago_accurate = today - relativedelta(years=10)

    # 打印结果
    # print("今天的日期:", today.strftime("%Y-%m-%d"))
    # print("十年前的日期（简单计算）:", ten_years_ago_simple.strftime("%Y-%m-%d"))
    # print("十年前的日期（精确计算）:", ten_years_ago_accurate.strftime("%Y-%m-%d"))

    return query_json('cn/index/fundamental', {
        "startDate": ten_years_ago_accurate.strftime("%Y-%m-%d"),
        "endDate": today.strftime("%Y-%m-%d"),
        "stockCodes": [
            stockCode
        ],
        "metricsList": [
            "pe_ttm.mcw"
        ]
    })


def get_etf_10year_pe():
    set_token("5356e78a-97e9-4dd8-9659-7b9550e31fa5", write_token=True)
    # 存储所有数据的字典
    all_data = {}

    #SZ，000001
    #zzHongLi，000922
    #全指金融，000992
    #qzYiYao，000991
    #zzYiLiao，399989
    #qzXiaoFei，000990
    #FoodDrink，000807
    #qzXinXi，000993
    #zzHuanBao，000827
    #YangLao，399812
    #zzJunGong，399967
    #zzChuanMei，399971

    # 自定义股票代码对应的名称
    etf_name_map = {
        "000001": "SZ",
        "000922": "zzHongLi",
        "000992": "qzJinRong",
        "000991": "qzYiYao",
        "399989": "zzYiLiao",
        "000990": "qzXiaoFei",
        "000807": "FoodDrink",
        "000993": "qzXinXi",
        "000827": "zzHuanBao",
        "399812": "YangLao",
        "399967": "zzJunGong",
        "399971": "zzChuanMei"
    }

    for item in etf_name_map.keys():
        print(item)
        result_pe_values= getPEValues(item)
        for entry in result_pe_values['data']:
            date_str = entry['date']
            # 去掉时区信息，假设所有时间为本地时间
            date_obj = datetime.fromisoformat(date_str[:-6])
            formatted_date = date_obj.strftime('%Y-%m-%d')  # 格式化日期为 YYYY-MM-DD
            stock_code = entry['stockCode']
            pe_value = round(entry['pe_ttm.mcw'], 2)  # 保留两位小数

            if stock_code not in all_data:
                all_data[stock_code] = []

            all_data[stock_code].append((formatted_date, pe_value))


    # 按日期排序每个 stockCode 的数据
    sorted_all_data = {}
    for stock_code, data_list in all_data.items():
        sorted_all_data[stock_code] = sorted(data_list, key=lambda x: x[0])

    # 分离日期和 pe_ttm.mcw
    dates_set = set()
    all_pe_values = {stock_code: [] for stock_code in sorted_all_data}

    for stock_code, data_list in sorted_all_data.items():
        for formatted_date, pe_value in data_list:
            dates_set.add(formatted_date)
            all_pe_values[stock_code].append(pe_value)


    # 将日期集合转换为有序列表
    dates = sorted(dates_set)

    # 创建 Line 图表实例
    line = (
        Line(init_opts=opts.InitOpts(width="3000px", height="1200px"))
        .add_xaxis(dates)
        .set_global_opts(
            title_opts=opts.TitleOpts(is_show=False),
            xaxis_opts=opts.AxisOpts(name="Date"),
            yaxis_opts=opts.AxisOpts(name="PE-TTM"),
            tooltip_opts=opts.TooltipOpts(trigger="axis"),  # 显示坐标轴触发提示框
            legend_opts=opts.LegendOpts(pos_bottom="0%")  # 将图例放在底部
        )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))  # 隐藏数据标签
    )

    # 为每个 stockCode 添加一条折线
    for stock_code, pe_values in all_pe_values.items():
        custom_name = etf_name_map.get(stock_code, stock_code)  # 获取自定义名称或默认名称
        line.add_yaxis(custom_name, pe_values, label_opts=opts.LabelOpts(is_show=False))

    # 渲染图表到 HTML 文件
    output_html_file="etf_10year_pe.html"
    line.render("etf_10year_pe.html")
    # 使用 snapshot-selenium 将 HTML 文件转换为图片
    output_image_file = "etf_10year_pe.png"
    output_image(output_html_file,output_image_file)

    send_email_with_image("etf_10year_pe","5908386@qq.com","5908386@qq.com","hakgazlgljxrbjbf","etf_10year_pe.png","etf_10year_pe")

# 检查当前模块是否是主程序
if __name__ == "__main__":
    get_etf_10year_pe()
