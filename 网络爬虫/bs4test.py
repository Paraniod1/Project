# -*- codeing = utf-8 -*-
# @Time : 2021/8/11 9:50
# @Author : chao
# @File : bs4test.py
# @Software : PyCharm

import re
from bs4 import BeautifulSoup

file = open("./baidu.html", 'rb')               # 打开当前目录下的文件 ./
html = file.read()                              # 读取文件并返回给html对象
bs = BeautifulSoup(html, "html.parser")         # html解析 并返回bs对象

print(bs.title)                                  # 打印出整个标签
print(bs.title.name)                             # 打印出标签的名字
print(bs.title.string)                           # 打印出标签的内容
list_a =bs.find_all("a")                         # 打印出所有标签 a的整个信息
for i in list_a:
    print(i)


for i in list_a:
     print(i.get("href"))                       # 打印出 a标签里面的超链接

for i in list_a:
    print(i.get_text())                         # 打印出a标签里面的文本值


# 1.tag(就是标签）  有两个属性 ：name ,attrs
print(bs.a.attrs)                               # 获取标签a的所有属性 以键值对返回
# 利用get()     传入属性的名称
print(bs.a['class'])    # 等价于 bs.a.get("class")


# 2.NavigableString (获取标签内部的文字） 用.string
print(bs.a.string)


# 3.BeautifulSoup 表示是一个文档的内容， 可以当中特殊的tag ,可以获取它的属性，类型，名称
print(bs.name)
print(bs.attrs)
print(type(bs))                      # <class 'bs4.BeautifulSoup'>

# 4.Comment 其对象是一个特殊类型的 NavigableString 对象，其输出的内容不包括注释符号。
print(bs.a.string)
print(type(bs.a.string))              # <class 'bs4.element.Comment'>

print(">>>>>>>>>>>>>>>>>>")
# 搜索 find_all(name, attrs, recursive, text, **kwargs) 过滤器

# （1）name  字符串过滤：会查找与字符串完全匹配的内容
# limit限制标签返回的数量    也可以使用find() 该函数返回一个
a_list = bs.find_all('a', limit = 3)                 # 查找 a标签
for i in a_list:
    print(i)

print(".............................")
# 正则表达式过滤 如果传入的是正则表达式，那么BeautifulSoup4会通过search()来匹配内容
t_list = bs.find_all(re.compile('a'))           # 查找所有与a相关的
for i in t_list:
    print(i)
print(".............................")
print(".............................")
# 通过类名
print(bs.select('.mnav'))
print(bs.select('.bri'))

# 通过标签名
print(bs.select('a'))

# 通过id
print(bs.select('#u1'))

# 通过组合
print(bs.select('div .bri'))   # div 下类名为bri

# 通过子标签
g_list = bs.select("head" > "title")

print(g_list)
