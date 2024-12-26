#import schedule
import time
from etf_000001_year_close import get_etf_000001_year_close
from etf_000016_year_close import get_etf_000016_year_close
from etf_000300_year_close import get_etf_000300_year_close
from etf_000688_year_close import get_etf_000688_year_close
from etf_000827_year_close import get_etf_000827_year_close
from etf_000852_year_close import get_etf_000852_year_close
from etf_000905_year_close import get_etf_000905_year_close
from etf_000922_year_close import get_etf_000922_year_close
from etf_000942_year_close import get_etf_000942_year_close
from etf_000990_year_close import get_etf_000990_year_close
from etf_000991_year_close import get_etf_000991_year_close
from etf_000993_year_close import get_etf_000993_year_close
from etf_10year_pe import get_etf_10year_pe
from etf_399006_year_close import get_etf_399006_year_close
from etf_399396_year_close import get_etf_399396_year_close
from etf_399812_year_close import get_etf_399812_year_close
from etf_399967_year_close import get_etf_399967_year_close
from etf_399971_year_close import get_etf_399971_year_close
from etf_399975_year_close import get_etf_399975_year_close
from etf_399989_year_close import get_etf_399989_year_close
from etf_932000_year_close import get_etf_932000_year_close
from etf_keypoint import get_etf_keypoint
from etf_year_close import get_etf_year_close

def get_all_etf_index():
    get_etf_year_close() #etf指数一年收盘价
    get_etf_keypoint()  #etf指数关键点位对比图
    get_etf_10year_pe() #etf指数10年PE
    get_etf_000001_year_close()
    get_etf_000016_year_close()
    get_etf_000300_year_close()
    get_etf_000688_year_close()
    get_etf_000827_year_close()
    get_etf_000852_year_close()
    get_etf_000905_year_close()
    get_etf_000922_year_close()
    get_etf_000942_year_close()
    get_etf_000990_year_close()
    get_etf_000991_year_close()
    get_etf_000993_year_close()
    get_etf_399006_year_close()
    get_etf_399396_year_close()
    get_etf_399812_year_close()
    get_etf_399967_year_close()
    get_etf_399971_year_close()
    get_etf_399975_year_close()
    get_etf_399989_year_close()
    get_etf_932000_year_close()
    print("get_all_etf_index done...")

# 检查当前模块是否是主程序
if __name__ == "__main__":
    get_all_etf_index
    # print("每天下午五点执行 job",flush=True)
    # # 每天下午五点执行 job 函数
    # schedule.every().day.at("17:00").do(get_all_etf_index)
    # print("定时任务已启动，等待每天下午五点执行...",flush=True)
    # while True:
    #     # print("正在运行...", flush=True)  # 添加 flush=True
    #     schedule.run_pending()
    #     time.sleep(60)  # 每分钟检查一次是否有任务需要执行


# lo.set_token("5356e78a-97e9-4dd8-9659-7b9550e31fa5", write_token=True)
#基础信息
# json_rltb = lo.query_json('cn/index', {
#     "stockCodes": [
#         "000001"
#     ]
# })
# print(json_rltb)
# #k线信息
# json_rltk = lo.query_json('cn/index/candlestick', {
#     "type": "normal",
#     "startDate": "2023-12-03",
#     "endDate": "2024-12-03",
#     "stockCode": "000001"
# })
# # print(json_rltk)
#
# # 提取日期和收盘价，并格式化日期
# dates = []
# closes = []
# for item in json_rltk['data']:
#     date_str = item['date']
#     # 去掉时区信息，假设所有时间为本地时间
#     date_obj = datetime.fromisoformat(date_str[:-6])
#     formatted_date = date_obj.strftime('%Y-%m-%d')  # 只保留日期部分
#     dates.append(formatted_date)
#     closes.append(item['close'])
#
# # print(dates)
# # print(closes)
#
# # 按时间倒序排列
# # sorted_data = sorted(zip(dates, closes), key=lambda x: x[0], reverse=True)
# # dates_sorted, closes_sorted = zip(*sorted_data)
# # 按时间正序排列
# sorted_data = sorted(zip(dates, closes), key=lambda x: x[0])
# dates_sorted, closes_sorted = zip(*sorted_data)
# # print(dates_sorted)
# # print(closes_sorted)
#
# # 创建Line对象
# line = (
#     Line()
#     .add_xaxis(dates_sorted)
#     .add_yaxis("收盘价", closes_sorted)
#     .set_global_opts(
#         title_opts=opts.TitleOpts(title="上证指数收盘价/年"),
#         xaxis_opts=opts.AxisOpts(type_="category", name="日期"),
#         yaxis_opts=opts.AxisOpts(name="收盘价", min_="dataMin", max_="dataMax")
#     )
#     .set_series_opts(
#         label_opts=opts.LabelOpts(is_show=False),
#         markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max"), opts.MarkPointItem(type_="min")]),
#         markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average")])
#     )
# )
#
# # 渲染图表到HTML文件
# line.render("stock_close_chart.html")

# # 提取日期和收盘价，并格式化日期
# extracted_data = []
# for item in json_rltk['data']:
#     date_str = item['date']
#     # 去掉时区信息，假设所有时间为本地时间
#     date_obj = datetime.fromisoformat(date_str[:-6])
#     formatted_date = date_obj.isoformat()
#     extracted_data.append((formatted_date, item['close']))
#
# # 打印结果
# for date, close in extracted_data:
#     print(f"Date: {date}, Close: {close}")


# # 提取日期和收盘价
# extracted_data = [(item['date'], item['close']) for item in json_rltk['data']]
#
# # 打印结果
# for date, close in extracted_data:
#     print(f"Date: {date}, Close: {close}")

# from pyecharts.charts import Bar
#
# bar = Bar()
# bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
# bar.add_yaxis("商家", [5, 20, 36, 10, 75, 90])
# # render 会生成本地 HTML 文件，默认会在当前目录生成 render.html 文件
# # 也可以传入路径参数，如 bar.render("mycharts.html")
# bar.render()

# from pyecharts.charts import Bar
# from pyecharts import options as opts
# # 内置主题类型可查看 pyecharts.globals.ThemeType
# from pyecharts.globals import ThemeType
#
# bar = (
#     Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK))
#     .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
#     .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
#     .add_yaxis("商家B", [15, 6, 45, 20, 35, 66])
#     .set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"))
# )
# bar.render()
