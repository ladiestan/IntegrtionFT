# coding:utf-8
import unittest
import requests
from sample.samplePackage import Blog
from common.logger import Log


class Test(unittest.TestCase):
    log = Log()

    def setUp(self):
        s = requests.sessions()
        self.blog = Blog(s)

    def test_login(self):
        u"""测试登录用例"""
        self.log.info("------start!------")
        result = self.blog.login()
        self.log.info(u"调用登录结果：%s" % result)
        self.log.info(u"获取是否登录成功:%s" % result["success"])
        self.assertEqual(result["success"], True)
        self.log.info("-------end-------")
