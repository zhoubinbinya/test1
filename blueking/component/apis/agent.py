# coding:utf-8
from ..base import ComponentAPI


# 系统API集合类的名称，一般为 Collections + 系统名
class CollectionsAGENT(object):

    def __init__(self, client):
        self.client = client

        # create_task为API名，method为请求API使用的方法，path为API路径，API域名为系统默认域名
        self.create_task = ComponentAPI(
            client=self.client, method='POST', path='/api/c/compapi/agent/create_task/',
            description=u'',
        )