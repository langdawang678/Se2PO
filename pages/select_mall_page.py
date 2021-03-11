from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locations.goods_lib_locations import GoodsLibLocations
from common.base_page import BasePage


class SelectMallPage(BasePage):

    # 退出元素是否存在
    def get_elements_exists(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(GoodsLibLocations.exit_link))
        except:
            return False
        else:
            return True
