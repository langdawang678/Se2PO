from selenium.webdriver.common.by import By


class LoginLocations:
    # 输入用户名
    user_input = (By.XPATH, '//input[@id="username"]')
    # 输入密码
    password_input = (By.XPATH, '//input[@id="passwd"]')
    # 登录按钮
    login_button = (By.XPATH, '//button[@type="submit"]')
