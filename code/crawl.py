# coding:utf-8
"""
Compatible for python2.x and python3.x
requirement: pip install requests
"""
from __future__ import print_function
import requests
import time
import json

def readFile(path):
    with open(path, "r+", encoding="utf-8") as f:
        data = f.read()
    f.close()
    output = data.split("\n")
    return output




if __name__ == "__main__":
    key_list = readFile("./data/usual.txt")
    # 请求示例 url 默认请求参数已经做URL编码
    my_api = "hozjXssqE2BSF0eaAxSPo7Vzs0emkEDJuJLZHNgbV8yvtWtwI3pNuZwgh97H2EBv"
    headers = {
        "Accept-Encoding": "gzip",
        "Connection": "close"
    }
    news_id = []
    lower_threshold = time.mktime(time.strptime("2020-1-8 00:00:00", "%Y-%m-%d %H:%M:%S"))
    # upper_threshold = time.mktime(time.strptime("2020-4-10 00:00:00", "%Y-%m-%d %H:%M:%S"))
    for key in key_list:
        print(key)
        """
        簇：1
        绘：8
        """
        pageToken = "1"
        flag = 0
        try_time = 0
        while 1:
            url = f"http://api01.idataapi.cn:8000/news/xinhuanet?kw={key}&pageToken={pageToken}&apikey={my_api}"
            try:
                print("Begin to read API")
                print(time.strftime('%Y-%m-%d %H:%M:%S'))
                r = requests.get(url, headers=headers)
                json_obj = r.json()
                print("Read successfully")
                print(key)
                if json_obj["retcode"] != "000000" and try_time < 3:
                    try_time += 1
                    continue
                elif try_time >= 3:
                    exit(-1)
            except Exception as e:
                print("Read json file error, the reason is ", e)
                continue

            print(try_time)

            try_time = 0
            try:
                with open(f"./data/news/{key}_{pageToken}.json", "w", encoding="utf-8") as f:
                    json.dump(json_obj, f, ensure_ascii=False)
            except Exception as e:
                print("Write into file error, the reason is ", e)

            try:
                pageToken = json_obj["pageToken"]
            except Exception as e:
                print("Don't have pageToken, the reason is ", e)

            timestamp = json_obj["data"][0]["publishDate"]
            print(pageToken, json_obj["data"][0]["publishDateStr"])
            if timestamp < lower_threshold:
                break
        # break