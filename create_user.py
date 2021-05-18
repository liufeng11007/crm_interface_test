# -*- coding: UTF-8 -*-
# @time     : 2021-03-11 10:20
# @Auther   : Aaron
# @File     : create_user.py

import json
import requests
import logging

from do_excel import DoExcel

logging.basicConfig(level=logging.NOTSET)

request_header = {
        "Authorization": "Bearer ImRj0mXjpjW8P6OJZItwGmrZcESclXyl79NrDG9tPPhHwNHgFBJLa7metPKmyydSTJpAUCgeE4M0xDRaoqhkP9w_AB-JnGHNhlvE7d5uqm493FqUVk1zDg3StnJcxns2Ptk9yqIPgieX_YL3kqve",
        "Accept": "application/json"
}

excel_filename = "create_user.xlsx"
sheet_name = "create_user"
doexcel = DoExcel(excel_filename, sheet_name)
data = doexcel.read_data()
print(type(data))
print(type(data[0].data))
print(data)


# data1 = {
#   "id": None,
#   "appParam": [
#     {
#       "appId": 3,
#       "enable": 1,
#       "sysAppLimits": [
#         {
#           "name": "限制消耗线索数",
#           "num": 1000,
#           "enable": 1
#         }
#       ]
#     },
#     {
#       "appId": 4,
#       "enable": 1,
#       "sysAppLimits": [
#
#       ]
#     }
#   ],
#   "bssOrgId": 33,
#   "directorId": None,
#   "name": "Auto0002",
#   "phone": "16902811012",
#   "roleId": 3
# }
# print(type(data1))
data1 = data[2].data
print(type(data1))
print(data1)
data_json = json.loads(data1)
# data_json = eval(data1)
print(type(data_json))
print(data_json)
url = "https://api-bfdev.staging.ukuaiqi.com/bifang/users/sysUser/create"

send_requset = requests.session()
# res = send_requset.post(url, headers=request_header, json=data_json)
# # print(res.json())
#
#
# logging.debug("请求反馈信息："+res.text)


# 创建部门
# p_url = "https://api-bfdev.staging.ukuaiqi.com/bifang/users/bssOrg/create"
#
# for i in range(1, 22):
#         p_data = {
#                 "name": "5大范甘迪0"+str(i),
#                 "parentId": 270
#         }
# p_data = {"name":"21","parentId":58}
#
# res = send_requset.post(p_url, headers=request_header, json=p_data)
# # logging.debug("请求反馈信息：请求次数--" + str(i)+",请求反馈结果：" + res.text)
# logging.debug("请求反馈信息：" + res.text)

# 修改部门名称
# up_url = "https://api-bfdev.staging.ukuaiqi.com/bifang/users/bssOrg/updateOrgName/71"
# up_data = {"name":"2222222222","parentId":71}
#
# res = send_requset.put(up_url, headers=request_header, json=up_data)
# logging.debug("请求反馈信息："+res.text)


# 删除部门

# for i in range(120,218):
#         d_url = "https://api-bfdev.staging.ukuaiqi.com/bifang/users/bssOrg/org/"+str(i)
#         res = send_requset.delete(d_url, headers=request_header)
#         logging.debug("请求反馈信息："+res.text)

# 新建角色

# r_url = "https://api-bfdev.staging.ukuaiqi.com/bifang/users/sysRole"
# for i in range(1,50):
#
#         r_data = {"name":"摇一摇"+str(i)}
#         res = send_requset.post(r_url, headers=request_header, json=r_data)
#         logging.debug("请求反馈信息：" + res.text)

# 新建用户
u_url = "https://api-bfdev.staging.ukuaiqi.com/bifang/users/sysUser/create"
u_data = {
  "id": None,
  "appParam": [
    {
      "appId": 3,
      "enable": 1,
      "sysAppLimits": [
        {
          "name": "限制消耗线索数",
          "num": 0,
          "enable": 1
        }
      ]
    },
    {
      "appId": 4,
      "enable": 1,
      "sysAppLimits": [

      ]
    }
  ],
  "bssOrgId": 330,
  "directorId": 0,
  "name": "森岛帆高",
  "phone": "133028110160",
  "roleId": 33
}
res = send_requset.post(u_url, headers=request_header, json=u_data)
logging.debug("请求反馈信息：" + res.text)



{
  "haveLeads": True,
  "pageSize": 20,
  "pageIndex": 1,
  "condition": "{\"must\":[{\"mobile\":[{\"exist\":\"1\"}]},{\"operateState\":[{\"eq\":[\"存续\",\"在业\"]}]},{\"businessLocation\":[{\"in\":[\"北京市\"]}]},{\"companyType\":[{\"eq\":[\"个体工商户\"]}]},{\"must\":[{\"jobName\":{\"in\":[\"收银员\"]}},{\"companyName\":{\"in\":[\"酒吧\",\"店\",\"美容\"]}}]}]}"
}