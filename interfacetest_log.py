# -*- coding: UTF-8 -*-
# @time     : 2021-03-17 11:08
# @Auther   : Aaron
# @File     : interfacetest_log.py

import logging


class DoLog:

    def __init__(self, name=None):
        if name is None:
            self.my_logger = logging.getLogger("testcase")
        else:
            self.my_logger = logging.getLogger(name)

        self.my_logger.setLevel("DEBUG")

        console_handler = logging.StreamHandler()
        console_handler.setLevel("DEBUG")

        file_handler = logging.FileHandler("testcase.log", encoding="utf-8")

        formater = logging.Formatter('%(asctime)s - [%(levelname)s] - [msg]: %(message)s - %(name)s - %(lineno)d')
        console_handler.setFormatter(formater)
        file_handler.setFormatter(formater)

        self.my_logger.addHandler(console_handler)
        self.my_logger.addHandler(file_handler)

    def get_logger(self):
        return self.my_logger


do_log = DoLog().get_logger()


if __name__ == '__main__':
    do_log = DoLog()
    my_logger = do_log.get_logger()
    my_logger.debug("这是一条debug级别的日志！")
    my_logger.info("这是一条info级别的日志！")
    my_logger.warning("这是一条warning级别的日志！")
    my_logger.error("这是一条error级别的日志！")
    my_logger.critical("这是一条critical级别的日志！")


