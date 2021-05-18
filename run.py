# -*- coding: UTF-8 -*-
# @time     : 2021-03-16 16:11
# @Auther   : Aaron
# @File     : run.py

import unittest

from HTMLTestRunnerNew import HTMLTestRunner


suite = unittest.defaultTestLoader.discover(r"F:\工作\python_scripts\crm3.0\Interface Test")
html_filename = r"F:\工作\python_scripts\crm3.0\Interface Test\crm3.0接口测试报告.html"

with open(html_filename, "wb") as file:
    runner = HTMLTestRunner(
        file,
        verbosity=1,
        title="crm3.0接口测试报告",
        description="新建用户、新建部门的接口测试",
        tester="aaron"

    )
    runner.run(suite)


