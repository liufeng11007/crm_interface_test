# -*- coding: UTF-8 -*-
# @time     : 2021-03-16 14:21
# @Auther   : Aaron
# @File     : test_createuser.py


import unittest
import ddt

from request import Request
from do_excel import DoExcel
from interfacetest_log import do_log


@ddt.ddt
class TestCreateUser(unittest.TestCase):
    """
    新建用户接口测试
    """

    excel_filename = "create_user.xlsx"
    sheet_name = "create_user"
    do_excel = DoExcel(excel_filename, sheet_name)
    testcases = do_excel.read_data()

    @classmethod
    def setUpClass(cls):

        cls.do_request = Request()
        request_header = {
            "Authorization": "Bearer yvXZbImBw1-PlsYl6aBAKS2Gw3GkKkfTTQ72kvne9ZGlQoT2g9ADhFGKzuN39UBkONr3BBl4aEcUhBrmuwPuTxB5kFlMaUPkXkbGRy80fbRQXk6NokAK2j6nLkT7C8wtoIwSJAY6463Z2Mt061O",
            "Accept": "application/json"
        }
        cls.do_request.add_header(request_header)

        do_log.info("开始执行用例")


    @classmethod
    def tearDownClass(cls):
        cls.do_request.close()
        do_log.info("用例执行结束")

    @ddt.data(*testcases)
    def test_create_user(self, one_testcase):
        res = self.do_request.send(one_testcase.method, one_testcase.url, json=one_testcase.data)
        actual_value = res.json()
        try:
            self.assertEqual(one_testcase.expected_value, actual_value.get("message"), "用例‘"+one_testcase.name+"’执行失败")
            self.do_excel.write_data(one_testcase, res.text, "成功")
        except AssertionError as e:
            do_log.error(f"具体异常是：{e}")
            self.do_excel.write_data(one_testcase, res.text, "失败")
            raise e


if __name__ == '__main__':
    unittest.main()

