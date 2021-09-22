# -*- codeing = utf-8 -*-
# @Time : 2021/8/11 11:50
# @Author : chao
# @File : retest.py
# @Software : PyCharm
import re

if __name__ == "__main__":
    # 1.compile(pattern)：创建模式对象
    # pat = re.compile("AAC")           # 创建匹配对象 也就是正则表达式
    # res = pat.search("adAAdsdAACda")  # 将正则表达式与search里面的匹配字符串进行比较 一般返回第一个位置
    # print(res)
    #
    #
    # # 2.search(pattern,string)：在字符串中寻找模式
    # # 不用创建匹配对象，直接寻找
    # m = re.search("AAC", "adAAdsdAACda")  #第一个参数是正则表达式 第二个是匹配字符串
    # print(m)
    #
    # # 3.sub(pat,repl,string) ：用repl替换 pat匹配项 (留的是中间的，因为中间在中心)
    # l = re.sub('a', 'S', "hhgaaahAnuaa")   #将第三个字符串中的a用S代替
    # print(l)

    # group() 匹配第一次出现的
    # pat_ = re.compile(^[abc]+)    # 开头是a,b,c的任意一个
    # k = pat_.search(defabc).group()
    # print(k)

    # 获取目的字符串
    a = re.match(r'(?P<first>\w+) (?P<second>\wt)', "Tom  Jan")
    a.group("first")     # Tom
    a.group(1)
    a.group("second")    # Jan
    a.group(2)