from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locations.login_locations import LoginLocations as loc
from common.base_page import BasePage


class LoginPage(BasePage):

    # 登录的元素定位、操作；
    def login(self, username, password):
        # WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.login_button))
        # self.driver.find_element(*loc.user_input).send_keys(username)
        # self.driver.find_element(*loc.password_input).send_keys(password)
        # self.driver.find_element(*loc.login_button).click()
        self.input_text(loc.user_input, username, "登录页面_输入用户名")
        self.input_text(loc.password_input, password, "登录页面_输入密码")
        self.click_element(loc.login_button, "登录页面_点击登录")

    # 获取错误信息的元素定位和操作
    def get_error_message(self):
        # 获取错误信息的文本值。 也需要等待。
        pass
