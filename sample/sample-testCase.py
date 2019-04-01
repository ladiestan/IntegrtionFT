# coding:utf-8
import unittest
import requests
from sample.samplePackage import Blog


class Test(unittest.TestCase):
    def setUp(self):
        s = requests.session()
        self.blog = Blog(s)

    def test_login(self):
        result = self.blog.login()
        print result
        print type(result)
        print result["success"]  # 登录，获取结果
        self.assertEqual(result["success"], True)  # 拿结果断言

    def test_del(self):
        # 第一步：登录
        self.blog.login()
        # 第二步：保存
        r2_url = self.blog.save(title="12121", body="WQASDAS")
        pid = self.blog.get_postid(r2_url)
        # 第三步：删除
        result = self.blog.del_tie(pid)
        self.assertEqual(result["isSuccess"], True)


if __name__ == "__main__":
    unittest.main()
