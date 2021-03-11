import time
import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.goods_lib_page import GoodsLibPage
from testdata import login_data, common_data


class TestLogin:

    def setup_class(self) -> None:
        # 访问登录页面
        self.driver = webdriver.Chrome()
        self.driver.get(common_data.base_url)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)

    def teardown_class(self) -> None:
        # self.driver.quit()
        print("***********")

    @pytest.mark.p0
    def test_login(self):
        # 登录
        # LoginPage(self.driver).login(*login_data.success)
        self.lp.login(*login_data.success)
        time.sleep(5)
        assert GoodsLibPage(self.driver).get_elements_exists()

        # 断言,元素是否存在 ；放在page中的单独方法中：高内聚低耦合。
        # pass

    # def test_login_error(self):
    #     # 步骤
    #     # 登录页面，登录操作
    #     # 断言
    #     # assert 错误的提示信息
    #     pass

# if __name__ == '__main__':
#     TestLogin().test_login()
