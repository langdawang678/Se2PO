# 正常场景
success = ("xxx", "xxx")
# 异常场景-数据驱动
abnormal = [
    {"user": "", "password": "python", "check": "请输入手机号"},
    {"user": "xxx", "password": "0", "check": "用户名或密码错误"},
    {"user": "xxx", "password": "python", "check": "手机号输入有误"},
]
