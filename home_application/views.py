# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云(BlueKing) available.
Copyright (C) 2017 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
"""
import re

from django.http import JsonResponse

from account.decorators import login_exempt
from common.mymako import render_mako_context
import xml.etree.ElementTree as ET

# @login_exempt
def home(request):
    """
    首页
    """
    from django import forms

    class UploadForm(forms.Form):
        file = forms.FileField()

    if request.method == "GET":
        return render_mako_context(request, '/home_application/index.html')
    if request.method == "POST":
        upload_form = UploadForm(request.POST, request.FILES)
        files_f = request.FILES['file']  # 获取上传的文件

        # 存放标签 标点符号 等错误行
        symbol_err_list = []
        # 存放 Server标签错误
        server_err_list = []

        try:
            # 读取xml文件 报错则表示xml文件内容错误
            xml = ET.parse(files_f)
        except Exception as e:

            e = str(e)
            # 获取报错的行数
            aa = re.findall(r'[0-9]{1,}', e)
            aa = int(aa[0])
            symbol_err_list.append(aa)

        # 读取上传文件的临时位置
        path_tem = files_f.temporary_file_path()
        # 对文件进行读的操作
        f = open(path_tem, "r")
        str1 = f.read()
        str1 = str1.split('\n')
        # 计数器
        server_nums = 0
        for i in range(0, len(str1)):
            server_hed = re.findall(r'<Server', str1[i])
            if server_hed:
                server_nums += 1
                # print(server_hed)
                # 如果连续两次 都是加的server 头 则证明 server尾错误
                if server_nums == 2:
                    server_nums = 1
                    server_err_list.append(i)

            server_tra = re.findall(r'</Server>', str1[i])

            if server_tra:
                server_nums -= 1

        if symbol_err_list and server_err_list:
            return JsonResponse({
                "code": 1,
                "msg": "标签或者符号错误{}行,Server错误在{}行上下！！".format(symbol_err_list[0], server_err_list)
            })

        elif symbol_err_list:
            return JsonResponse({
                "code": 1,
                "msg": "标签或者符号错误{}行！！".format(symbol_err_list[0])
            })

        elif server_err_list:
            return JsonResponse({
                "code": 1,
                "msg": "Server错误在{}行上下！！".format(server_err_list)
            })

        return JsonResponse({
            "code": 0,
            "msg": "没有发现问题!!",
        })


@login_exempt
def dev_guide(request):
    """
    开发指引
    """
    return render_mako_context(request, '/home_application/dev_guide.html')

@login_exempt
def contactus(request):
    """
    联系我们
    """
    return render_mako_context(request, '/home_application/contact.html')
