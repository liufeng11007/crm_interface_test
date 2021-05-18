# -*- coding: UTF-8 -*-
# @time     : 2021-03-15 16:06
# @Auther   : Aaron
# @File     : request.py

import json
import requests
from do_excel import DoExcel


class Request:

    def __init__(self):
        self.session = requests.session()

    def send(self, method, url, **kwargs):
        """
        发送请求的方法
        :param method: 请求方法
        :param url: 请求url
        :param kwargs: headers请求头字典，data、json、files
        :return:
        """
        one_method = method.upper()
        kwargs["json"] = self.do_param("json", kwargs)
        kwargs["data"] = self.do_param("data", kwargs)
        return self.session.request(one_method, url, **kwargs)

    @staticmethod
    def do_param(param_name, param_dict):

        if param_name in param_dict:
            data = param_dict.get(param_name)
            # isinstance() 函数判断一个对象是否是一个已知的类型，类似 type()。
            if isinstance(data, str):
                try:
                    data = json.loads(data)
                except Exception:
                    data = eval(data)
            return data

    def add_header(self, one_dict):
        """
        添加公共的请求头
        :param one_dict: 请求头参数，字典类型
        :return:
        """
        self.session.headers.update(one_dict)

    def close(self):
        """

        :return:
        """
        self.session.close()


if __name__ == '__main__':
    excel_filename = "create_user.xlsx"
    sheet_name = "create_user"
    doexcel = DoExcel(excel_filename, sheet_name)
    data = doexcel.read_data()
    request_header = {
        "Authorization": "Bearer GIGGXI0XSkW3aKxys8xPYxPNP6xAG4mT8sLwJYJvRCOrDD8dZdlcE1wOTmPCglC4n0HxwX9cQ8s3Jbas-rFFOK9ybQdmBc7xvaCGupVfwB3VKaCQDKn1o8hzktg4Im1hw7xWTih",
        "Accept": "application/json"
    }
    create_user = Request()
    create_user.add_header(request_header)
    res = create_user.send(data[0].method, data[0].url, json=data[0].data)
    print(res.json())
    doexcel.write_data(data[0], res.json()["message"], "成功")

