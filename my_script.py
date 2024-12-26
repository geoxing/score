# my_script.py
import sys
import time

def main():
    while True:
        print("正在运行...", flush=True)  # 添加 flush=True
        time.sleep(60)  # 每分钟打印一次

if __name__ == "__main__":
    main()
