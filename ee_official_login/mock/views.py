# coding:utf-8
from conf.default import REDIRECT_FIELD_NAME


def login(request):
    """
    登录处理
    """
    # 获取 ?c_url=xxx 登录成功跳转目的地址
    redirect_to = request.GET.get(REDIRECT_FIELD_NAME, '')

    # 复用bkauth的登录页面
    # POST 请求
    if request.method == "POST":
        # 获取用户名密码
        form = BkAuthenticationForm(request, data=request.POST)

        username = form.data["username"]
        password = form.data["password"]

        # 执行校验
        # will call MockBackend.authenticate
        user = authenticate(username=username, password=password)

        # 失败
        if user is None:
            logger.debug("custom_login:mock user is None, will redirect_to=%s", redirect_to)
            # 直接调用蓝鲸登录失败处理方法
            return login_failed_response(request, redirect_to, app_id=None)

        # 成功，则调用蓝鲸登录成功的处理函数，并返回响应
        logger.debug("custom_login:mock login success, will redirect_to=%s", redirect_to)
        return login_success_response(request, user, redirect_to, app_id=None)
    # GET
    else:
        # 构造前端表单需要的数据
        form = BkAuthenticationForm(request)
        current_site = get_current_site(request)
        context = {
            'form': form,
            REDIRECT_FIELD_NAME: redirect_to,
            'site': current_site,
            'site_name': current_site.name,

            # set to default; 复用account/login.html表单
            'error_message': "",
            'app_id': "",
            'is_license_ok': True,
            'reset_password_url': "",
            'login_redirect_to': "",
        }

        # 跳转登录页
        template_name = 'account/login.html'
        response = TemplateResponse(request, template_name, context)

        # 清空 bk_token
        response = set_bk_token_invalid(request, response)
        return response
