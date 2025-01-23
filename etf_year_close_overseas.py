from tools import output_image, send_email_with_image, get_etf_year_close_line_all_overseas

def get_etf_year_close_overseas():
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
    line= get_etf_year_close_line_all_overseas(etf_info_map)
    # 渲染图表到 HTML 文件
    output_html_file="etf_year_close_overseas.html"
    line.render(output_html_file)
    # 使用 snapshot-selenium 将 HTML 文件转换为图片
    output_image_file = "etf_year_close_overseas.png"
    output_image(output_html_file,output_image_file)

    send_email_with_image("etf_year_close_overseas","5908386@qq.com","5908386@qq.com","hakgazlgljxrbjbf","etf_year_close_overseas.png","etf_year_close_overseas")


# 检查当前模块是否是主程序
if __name__ == "__main__":
    get_etf_year_close_overseas()