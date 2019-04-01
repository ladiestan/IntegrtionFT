# coding:utf-8
from bs4 import BeautifulSoup
import requests

r = requests.get("http://www.cnblogs.com/yoyoketang/")
# 请求首页后获取整个 html 界面
blog = r.content
# 用 html.parser 解析 html
soup = BeautifulSoup(blog, "html.parser")
# find 方法查找页面上第一个属性匹配的 tag 对象
tag_soup = soup.find(class_="c_b_p_desc")
# len 函数获取子节点的个数
print len(tag_soup.contents)
# print len(list(tag_soup.children))
# 获取子孙节点的个数
print len(list(tag_soup.descendants))
for i in tag_soup.descendants:
    print i
# 循环打印出子节点
for i in tag_soup.contents:
    print i
# 通过下标取出第 1 个 string 子节点
print tag_soup.contents[0]
# 通过下标取出第 2 个 a 子节点
print tag_soup.contents[1]
