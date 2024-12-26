import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot as driver
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from pyecharts import options as opts
from pyecharts.charts import Line
from pyecharts.globals import ThemeType

set_token("5356e78a-97e9-4dd8-9659-7b9550e31fa5", write_token=True)

def getClosePoint(stockCode="000001"):
    # 获取当前日期
    today = datetime.today()
    # 计算十年前的日期（简单计算）
    ten_years_ago_simple = today - timedelta(days=10 * 365)

    # 计算十年前的日期（精确计算）
    one_years_ago_accurate = today - relativedelta(years=1)

    # 打印结果
    # print("今天的日期:", today.strftime("%Y-%m-%d"))
    # print("十年前的日期（简单计算）:", ten_years_ago_simple.strftime("%Y-%m-%d"))
    # print("十年前的日期（精确计算）:", ten_years_ago_accurate.strftime("%Y-%m-%d"))
    #k线信息
    return query_json('cn/index/candlestick', {
        "type": "normal",
        "startDate": one_years_ago_accurate.strftime("%Y-%m-%d"),
        "endDate": today.strftime("%Y-%m-%d"),
        "stockCode": stockCode
    })

def get_etf_year_close_line(etf_info_map):
    all_data = {}
    for item in etf_info_map.keys():
        print(item)
        result_close_points= getClosePoint(item)
        for entry in result_close_points['data']:
            date_str = entry['date']
            # 去掉时区信息，假设所有时间为本地时间
            date_obj = datetime.fromisoformat(date_str[:-6])
            formatted_date = date_obj.strftime('%Y-%m-%d')  # 格式化日期为 YYYY-MM-DD

            stock_code = item
            close_point = round(entry['close'])  # 保留两位小数

            if stock_code not in all_data:
                all_data[stock_code] = []

            all_data[stock_code].append((formatted_date, close_point))


    # 按日期排序每个 stockCode 的数据
    sorted_all_data = {}
    for stock_code, data_list in all_data.items():
        sorted_all_data[stock_code] = sorted(data_list, key=lambda x: x[0])

    # 分离日期和 pe_ttm.mcw
    dates_set = set()
    all_close_points = {stock_code: [] for stock_code in sorted_all_data}

    for stock_code, data_list in sorted_all_data.items():
        for formatted_date, close_point in data_list:
            dates_set.add(formatted_date)
            all_close_points[stock_code].append(close_point)


    # 将日期集合转换为有序列表
    dates = sorted(dates_set)

    # 创建 Line 图表实例
    line = (
        Line(init_opts=opts.InitOpts(width="2400px", height="1200px"))
        .add_xaxis(dates)
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))  # 隐藏数据标签
    )

    # 为每个 stockCode 添加一条折线
    for stock_code, close_point in all_close_points.items():
        etf_info=etf_info_map.get(stock_code, stock_code)
        etf_name = etf_info.get("name")  # 获取自定义名称或默认名称
        # 打印数据范围
        min_value = min(close_point)
        max_value = max(close_point)
        line.add_yaxis(etf_name,
                       close_point,
                       symbol_size=0,  # 设置数据点大小为0
                       markline_opts=opts.MarkLineOpts(
                           data=[
                               opts.MarkLineItem(
                                   y=etf_info.get("major_support"),
                                   name="major_support",
                                   linestyle_opts=opts.ItemStyleOpts(
                                       color="#00da3c",  # 红色
                                       border_width=2   # 宽度为2像素
                                   )
                               ),
                               opts.MarkLineItem(
                                   y=etf_info.get("minor_support"),
                                   name="minor_support",
                                   linestyle_opts=opts.ItemStyleOpts(
                                       color="lightgreen",  # 红色
                                       border_width=2   # 宽度为2像素
                                   )
                               ),
                               opts.MarkLineItem(
                                   y=etf_info.get("minor_pressure"),
                                   name="minor_pressure",
                                   linestyle_opts=opts.ItemStyleOpts(
                                       color="lightpink",  # 红色
                                       border_width=2   # 宽度为2像素
                                   )
                               ),
                               opts.MarkLineItem(
                                   y=etf_info.get("major_pressure"),
                                   name="major_pressure",
                                   linestyle_opts=opts.ItemStyleOpts(
                                       color="ec0000",  # 红色
                                       border_width=2   # 宽度为2像素
                                   )
                               ),
                           ],
                       ),
                       label_opts=opts.LabelOpts(is_show=True))
    # 设置全局选项
    line.set_global_opts(
        title_opts=opts.TitleOpts(is_show=True),
        tooltip_opts=opts.TooltipOpts(trigger="axis"),  # 显示坐标轴触发提示框
        yaxis_opts=opts.AxisOpts(
            type_="value",
            min_=min_value,  # 明确设置最小值
            max_=max_value ,  # 明确设置最大值
        ),
        legend_opts=opts.LegendOpts(is_show=True)  # 隐藏图例
    )
    return line

def send_email_with_image(subject, sender, receiver, password, image_path, message):
    # 创建一个MIMEMultipart对象
    msg = MIMEMultipart()
    msg['From'] = Header(sender)
    msg['To'] = Header(receiver)
    msg['Subject'] = Header(subject)

    # 邮件正文内容
    body = MIMEText(message, 'plain', 'utf-8')
    msg.attach(body)

    # 打开图片文件，并将其作为附件添加到邮件中
    with open(image_path, 'rb') as f:
        img = MIMEImage(f.read())
        # 给图片附件命名
        img.add_header('Content-ID', '<image1>')
        msg.attach(img)

    # 连接到SMTP服务器并发送邮件
    try:
        server = smtplib.SMTP_SSL('smtp.qq.com', 465)  # 使用你的SMTP服务器地址和端口
        server.login(sender, password)  # 登录邮箱
        server.sendmail(sender, [receiver], msg.as_string())
        server.quit()
        print(subject+"->邮件发送成功")
    except smtplib.SMTPException as e:
        print(subject+"->邮件发送失败", e)

def output_image(output_html_file,output_image_file):
    # 使用自定义的 chrome_options
    make_snapshot(driver, output_html_file, output_image_file)
