# -*- codeing = utf-8 -*-
# @Time : 2021/8/10 16:24
# @Author : chao
# @File : urllibtest.py
# @Software : PyCharm

import urllib.request
import urllib.parse
import urllib.request

# 获取网页

# 1.get请求

# url = "https://movie.douban.com/top250?start=0&filter="
# url = "https://www.csdn.net/?spm=1001.2101.3001.5359"
# respense = urllib.request.urlopen(url)
# print(respense.read().decode("utf-8"))

# 2.post请求   data参数用于post请求，比如表单提交，如果没有data参数则是get请求

# url = "https://www.baidu.com/"
# data = bytes(urllib.parse.urlencode({'好好学习': '天天向上'}), encoding = 'utf-8')  # urlencode将字典解码，并转化为字节类型
# respense = urllib.request.urlopen(url, data = data, timeout = 1)                 # timeout 服务器响应时间设置
# print(respense.read().decode("utf-8"))

# url = "https://www.baidu.com/"
#
# headers ={
# "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67",
#
# "Host": "www.baidu.com", "Referer": "https://cn.bing.com/"
#
# }
#
# dict = {"name": "tom"}
#
# data = bytes(urllib.parse.urlencode(dict), encoding = "utf-8") # 转为字节类型
#
#
# # 由于urlopen无法传参数，声明一个Request对象
# request = urllib.request.Request(url, data = data, headers = headers, method = 'POST')
# respense = urllib.request.urlopen(request)
# print(respense.read().decode('utf-8'))


# 访问一个指定的网址
def askURL(url):
    # 模拟浏览器头部信息，向豆瓣服务器发送消息
    head = {  # 用户代理 表示告诉豆瓣服务器，我们是什么类型的 机器，浏览器
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 92.0 .4515.131Safari / 537.36Edg / 92.0.902.67"
    }

    request = urllib.request.Request(url, headers = head)    # 返回一个对象
    html = ""
    try:
        respense = urllib.request.urlopen(request)
        html = respense.read().decode('utf-8')
        print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)

    return html

if __name__ =="__main__":
    askURL("https://movie.douban.com/top250?start=0&filter=")