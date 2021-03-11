from common.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locations.goods_lib_locations import GoodsLibLocations


class GoodsLibPage(BasePage):

    # 检查登录后的元素是否存在
    def get_elements_exists(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(GoodsLibLocations.goods_lib))
        except:
            return False
        else:
            return True

    # 获取错误信息的元素定位和操作
    def get_error_message(self):
        pass
