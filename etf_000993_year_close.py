from tools import output_image, send_email_with_image, get_etf_year_close_line

def get_etf_000993_year_close():
    etf_info_map = {
        # "000001": {"name":"上证指数","major_support":2720,"minor_support":3000,"minor_pressure":3600,"major_pressure":4000},
        # "000016": {"name":"上证50","major_support":2297,"minor_support":2610,"minor_pressure":3000,"major_pressure":3640},
        # "000300": {"name":"沪深300","major_support":3000,"minor_support":3430,"minor_pressure":4200,"major_pressure":5400},
        # "000905": {"name":"中证500","major_support":4700,"minor_support":5195,"minor_pressure":6400,"major_pressure":8100},
        # "000852": {"name":"中证1000","major_support":4400,"minor_support":5400,"minor_pressure":8500,"major_pressure":12000},
        # "932000": {"name":"中证2000","major_support":1700,"minor_support":2070,"minor_pressure":2142,"major_pressure":2635},
        # "399006": {"name":"创业板","major_support":1250,"minor_support":1750,"minor_pressure":2422,"major_pressure":3400},
        # "000688": {"name":"科创50","major_support":345,"minor_support":518,"minor_pressure":1300,"major_pressure":1726},
        # "000922": {"name":"中证红利","major_support":3476,"minor_support":3600,"minor_pressure":4890,"major_pressure":6200},
        # "000991": {"name":"全指医药","major_support":7200,"minor_support":9400,"minor_pressure":13000,"major_pressure":17300},
        # "399989": {"name":"中证医疗","major_support":5630,"minor_support":8570,"minor_pressure":13000,"major_pressure":18000},
        # "399812": {"name":"养老产业","major_support":4800,"minor_support":7100,"minor_pressure":10000,"major_pressure":13000},
        # "000990": {"name":"全指消费","major_support":7000,"minor_support":12372,"minor_pressure":15000,"major_pressure":27300},
        # "000942": {"name":"内地消费","major_support":6400,"minor_support":8750,"minor_pressure":11000,"major_pressure":17300},
        # "399396": {"name":"食品饮料","major_support":7000,"minor_support":12210,"minor_pressure":16500,"major_pressure":30000},
        # "000827": {"name":"中证环保","major_support":1200,"minor_support":1415,"minor_pressure":2300,"major_pressure":3000},
        "000993": {"name":"全指信息","major_support":3900,"minor_support":4462,"minor_pressure":6300,"major_pressure":7500},
        # "399971": {"name":"中证传媒","major_support":931,"minor_support":1220,"minor_pressure":1700,"major_pressure":2000},
        # "399967": {"name":"中证军工","major_support":6400,"minor_support":8300,"minor_pressure":12600,"major_pressure":15000},
        # "399975": {"name":"证券公司","major_support":500,"minor_support":600,"minor_pressure":800,"major_pressure":1600},
        # "HSI": {"name":"恒生指数","major_support":14863,"minor_support":18415,"minor_pressure":25000,"major_pressure":33000},
        # "H30533": {"name":"中概互联","major_support":3415,"minor_support":5122,"minor_pressure":8000,"major_pressure":17000},
        # "H11136": {"name":"中国互联","major_support":2500,"minor_support":3739,"minor_pressure":7500,"major_pressure":12463},
        # "HSTECH": {"name":"恒生科技","major_support":2200,"minor_support":3300,"minor_pressure":7600,"major_pressure":10000},
        # "HSHCI": {"name":"恒生医疗","major_support":2168,"minor_support":2340,"minor_pressure":2900,"major_pressure":4300},
        # "00700": {"name":"腾讯","major_support":140,"minor_support":290,"minor_pressure":420,"major_pressure":700},
        # "GDAXI": {"name":"德国dax","major_support":8200,"minor_support":11000,"minor_pressure":15000,"major_pressure":20000},
        # "SPX": {"name":"标普500","major_support":2000,"minor_support":2300,"minor_pressure":5254,"major_pressure":6000},
        # "IXIC": {"name":"纳斯达克","major_support":4800,"minor_support":6800,"minor_pressure":16000,"major_pressure":20000},
        # "NDX": {"name":"纳斯达克100","major_support":4200,"minor_support":7000,"minor_pressure":18000,"major_pressure":21000},
        # "518880": {"name":"黄金etf","major_support":2.7,"minor_support":3.2,"minor_pressure":5.3,"major_pressure":6.2},
        # "USDCNH": {"name":"美元人民币","major_support":6.8,"minor_support":7.08,"minor_pressure":7.25,"major_pressure":7.37},
        # "JPYCNY": {"name":"日元人民币","major_support":4.45,"minor_support":4.6,"minor_pressure":6,"major_pressure":6.7}
    }
    line= get_etf_year_close_line(etf_info_map)
    # 渲染图表到 HTML 文件
    output_html_file="etf_000993_year_close.html"
    line.render(output_html_file)
    # 使用 snapshot-selenium 将 HTML 文件转换为图片
    output_image_file = "etf_000993_year_close.png"
    output_image(output_html_file,output_image_file)

    send_email_with_image("etf_全指信息_year_close","5908386@qq.com","5908386@qq.com","hakgazlgljxrbjbf","etf_000993_year_close.png","etf_全指信息_year_close")

# 检查当前模块是否是主程序
if __name__ == "__main__":
    get_etf_000993_year_close()