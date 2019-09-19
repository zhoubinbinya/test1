# -*- coding: utf-8 -*-
# 蓝鲸登录方式：bk_login
# 企业内部Username-password登录方式：enterprise_ldap
# 自定义登录方式：custom_login
LOGIN_TYPE = 'custom_login'

# 默认bk_login，无需设置其他配置

##################################################
# 企业内部Username-password登录 enterprise_ldap    #
# 该方式需要自行搭建对接蓝鲸登录和企业内部登录的中间服务   #
#################################################
# 对接企业内部登录的服务URL
# 对应验证API URL: ACCESS_LOGIN_SERVICE_URL+'validate_user/' 对应获取用户信息API URL: ACCESS_LOGIN_SERVICE_URL+'get_user_info/'
ACCESS_LOGIN_SERVICE_URL = ''  # 例如： http://127.0.0.1:12306/
# 接口鉴权用的secret key，自行约定，保证接口能调用成功即可
ACCESS_LOGIN_SERVICE_API_SECRET_KEY = ''
# 请求接口默认超时时间，单位毫秒(ms)，默认1.5s
ACCESS_LOGIN_SERVICE_API_REQUEST_TIMEOUT = 1500


###########################
# 自定义登录 custom_login   #
###########################
# 配置自定义登录请求和登录回调的响应函数, 如：CUSTOM_LOGIN_VIEW = 'ee_official_login.oauth.google.views.login'
CUSTOM_LOGIN_VIEW = 'ee_official_login.mock.views.login'
# 配置自定义验证是否登录的认证函数, 如：CUSTOM_AUTHENTICATION_BACKEND = 'ee_official_login.oauth.google.backends.OauthBackend'
CUSTOM_AUTHENTICATION_BACKEND = ''
