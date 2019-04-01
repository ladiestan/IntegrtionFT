# coding:utf-8
import requests
from common.logger import Log
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Login():
    # s = requests.sessions()# 全局参数
    log = Log()

    def __init__(self, s):
        self.s = s

    def login(self):
        '''登录接口'''
        url = "https://passport.cnblogs.com/user/signin"
        header = {  # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0",
            # "Accept": "application/json, text/javascript, */*; q=0.01",
            # "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
            # "Accept-Encoding": "gzip, deflate, br",
            # "Content-Type": "application/json; charset=utf-8",
            # "VerificationToken": "xxx 已省略",
            "Cookie": "xxx 已省略",
            "X-Requested-With": "XMLHttpRequest",
            # "Connection":"keep-alive",
            # "Content-Length":"385"
        }
        json_data = {"input1": "账号",
                     "input2": "密码",
                     "remember": False}
        res = self.s.post(url, headers=header, json=json_data, verify=False)
        result1 = res.content  # 字节输出
        print result1
        return res.json()