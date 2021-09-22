# -*- codeing = utf-8 -*-
# @Time : 2021/8/10 21:50
# @Author : chao
# @File : 豆瓣爬虫.py
# @Software : PyCharm

# 1.爬取网页
# 2.逐一解析数据
# 3.保存数据


import urllib.request
import urllib.parse
import urllib.request
import urllib.error
import re
from bs4 import BeautifulSoup
import xlwt

# 影片详情链接的正则表达式
findLink = re.compile(r'<a href="(.*?)">')                                             # .*? 懒惰模式正则 匹配到第一个就不匹配了
# 影片图片链接
findImage = re.compile(r'<img.*src="(.*?)"', re.S)                                  # re.S 将包含换行的字符看成一个整体
# 影片的标题
findTitle = re.compile(r'<span class="title">(.*)</span>')
# 影片评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')  # 评分含小数点当成字符串 不用\d
# 影片评价人数
findJudge = re.compile(r'<span>(\d*)人评价</span>')                                     # 人数全是整数 用\d
# 影片的概述
findInq = re.compile(r'<span class="inq">(.*)</span>')
# 影片相关内容
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)


# 访问一个指定的网址
def askURL(url):
    # 模拟浏览器头部信息，向豆瓣服务器发送消息
    head = {  # 用户代理 表示告诉豆瓣服务器，我们是什么类型的 机器，浏览器
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 92.0 .4515.131Safari / 537.36Edg / 92.0.902.67"
    }

    request = urllib.request.Request(url, headers=head)    # 返回一个对象
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf-8')

    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)

    return html

# 爬取网页
def getData(baseurl):
    datalist = []
    for i in range(0, 10):
        url = baseurl + str(i*25)     # 通过start = 25的倍数 获取10页的信息
        html = askURL(url)            # 保持获取到的源码数据

    # 2.逐一解析数据
    soup = BeautifulSoup(html, "html.parser")                # html解析 并返回bs对象
    for item in soup.find_all('div', class_="item"):         # 查找符合要求的字符串 返回一个列表
        # print(item)
        data = [ ]                                            # 保持一部影片的信息
        item = str(item)                                     # 将得到的列表转为字符串 以便用正则表达式

        link = re.findall(findLink, item)[0]                 # re库用来通过正则表达式查找指定的字符串 返回找到第一个 item为查找字符串
        data.append(link)                                    # 将链接加入data中

        image = re.findall(findImage, item)[0]               # 影片图片链接
        data.append(image)

        titles = re.findall(findTitle, item)                 # 片名可能有的有中文，英文，有的没有
        if (len(titles) == 2):
            ctitle = titles[0]                               # 中文名
            data.append(ctitle)
            otitle = titles[1].replace("/", "")              # 去掉其他符号 用空格代替
            data.append(otitle)                               # 英文名
        else:
            data.append(titles[0])
            data.append("")                                 # 英文名留空，为后面xlsl存储做准备

        rating = re.findall(findRating, item)[0]              # 评分
        data.append(rating)

        num = re.findall(findJudge, item)[0]                 # 评价人数
        data.append(num)

        inq = re.findall(findInq, item)                      # 影片概述 有的可能没有
        if (len(inq) != 0):
            inq = inq[0].replace("。", "")                   # 去掉句号
            data.append(inq)
        else:
            data.append(" ")                                 # 留空

        bd = re.findall(findBd, item)[0]                      # 影片相关内容
        bd = re.sub('<br(\s+)?/>(\s+)?', " ", bd)             # 去掉<br/>
        bd = re.sub('/', " ", bd)                             # 替换/
        data.append(bd.strip())                               # 去掉前后的空格

        datalist.append(data)
    #print(datalist)
    return datalist

# 保存数据
def saveData(datalist, savepath):
    print("save.....")
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)            # 创建workbook对象,也就是一个文件
    sheet = book.add_sheet("豆瓣电影250Top", cell_overwrite_ok=True)           # 支持重写覆盖  创建工作表
    col = ("电影详情链接", "图片链接", "影片中文名", "影片外国名", "评分", "评价数", "概况", "相关信息")
    # 写第一行表单内容
    for i in range(0, 8):
        sheet.write(0, i, col[i])
    for i in range(0, 250):
        print("第%d条数据存储完毕" % (i+1))
        data = datalist[i]                                                       # 每条电影的信息
        for j in range(0, 8):
            sheet.write(i+1, j, data[j])                                         # 存数据

    book.save(savepath)



def main():
    # 目标网址
    baseurl = "https://movie.douban.com/top250?start="
    # 1.爬取网页
    datalist = getData(baseurl)
    # 3.保存数据
    savapath = "豆瓣电影Top250w.xls"
    saveData(datalist, savapath)


if __name__ == "__main__":
    main()
