from tools import output_image, send_email_with_image, get_etf_year_close_line_money

def get_etf_GOLD_year_close():
    etf_info_map = {
        "518880.SS": {"name":"Gold","major_support":2.7,"minor_support":3.2,"minor_pressure":5.3,"major_pressure":6.2},
        # "USDCNY=X": {"name":"USD","major_support":6.8,"minor_support":7.08,"minor_pressure":7.25,"major_pressure":7.37},
        # "JPYCNY=X": {"name":"JPY","major_support":4.45,"minor_support":4.6,"minor_pressure":6,"major_pressure":6.7}
    }
    line= get_etf_year_close_line_money(etf_info_map)
    # 渲染图表到 HTML 文件
    output_html_file="etf_GOLD_year_close.html"
    line.render(output_html_file)
    # 使用 snapshot-selenium 将 HTML 文件转换为图片
    output_image_file = "etf_GOLD_year_close.png"
    output_image(output_html_file,output_image_file)

    send_email_with_image("etf_GOLD_year_close","5908386@qq.com","5908386@qq.com","hakgazlgljxrbjbf","etf_GOLD_year_close.png","etf_GOLD_year_close")


# 检查当前模块是否是主程序
if __name__ == "__main__":
    get_etf_GOLD_year_close()