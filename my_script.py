# my_script.py
import sys
import time
# 导入所需库
import yfinance as yf

from datetime import datetime, timedelta

etfs = {
    "恒生ETF": "02800.HK",   # 盈富基金（港股）
    "标普500ETF": "SPY",     # 标普500 ETF
    "纳斯达克ETF": "QQQ",    # 纳斯达克100 ETF
    "美债ETF": "TLT",        # 长期美债ETF
}

def get_daily_close(etf_code):
    etf = yf.Ticker(etf_code)
    data = etf.history(period="1d")  # 获取当日分钟/小时数据
    return data["Close"].values[0] if not data.empty else None

def get_1year_history(etf_code):
    etf = yf.Ticker(etf_code)
    data = etf.history(period="1y")  # 获取过去1年数据
    return data["Close"]

def get_10year_history(etf_code):
    etf = yf.Ticker(etf_code)
    data = etf.history(period="10y")  # 获取过去10年数据
    return data["Close"]



def main():
    # 示例：查询恒生ETF当日收盘价
    hk_close_price = round(get_daily_close("^HSI"), 2)
    print(f"恒生ETF当日收盘价: {hk_close_price}")

    # 示例：获取标普500 ETF过去一年收盘价
    # hk_1y_close_price = get_1year_history("H30533.SS")
    # for date, price in hk_1y_close_price.items():
    #     # date_obj = datetime.fromisoformat(date.date())
    #     formatted_date = date.date().strftime('%Y-%m-%d')  # 格式化日期为 YYYY-MM-DD
    #     close_point=round(price)  # 保留两位小数
    #     print(f"日期: {formatted_date}, 收盘价: {close_point}")

    # # 示例：获取纳斯达克ETF过去十年收盘价
    # qqq_10y = get_10year_history("QQQ")
    # print(qqq_10y)

    # while True:
    #     print("正在运行...", flush=True)  # 添加 flush=True
    #     time.sleep(60)  # 每分钟打印一次

if __name__ == "__main__":
    main()
