# coding:utf-8
import unittest
import requests
import urllib3

# 禁用安全请求警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Blog_login(unittest.TestCase):
    def login(self, username, psw, reme=True):
        '''三个参数： 账号： username，密码： psw,记住登录： reme=True'''
        url = "https://passport.cnblogs.com/user/signin"
        header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0)Gecko/20100101 Firefox/44.0",
                  "Cookie": "xxx 已省略",
                  "X-Requested-With": "XMLHttpRequest",
                  "Connection": "keep-alive",
                  "Content-Length": "385"
                  }
        json_data = {"input1": username,
                     "input2": psw,
                     "remember": reme}
        res = requests.post(url, headers=header, json=json_data, verify=False)
        result1 = res.content  # 字节输出Python

        print result1
        return res.json()  # 返回 json

        def test_login1(self):
        '''测试登录：正确账号，正确密码'''
        username = "正确账号，抓包获得的加密字符串",
        psw = "正确密码，抓包获得的加密字符串",
        result = self.login(username, psw)
        self.assertEqual(result["success"], True)

        def test_login2(self):

        '''测试登录：正确账号，错误密码'''
        username = "正确账号",
        psw = "xxx 错误密码",
        result = self.login(username, psw)
        self.assertEqual(result["success"], False)


if __name__ == "__main__":
    unittest.main()
