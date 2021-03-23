from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging  # 这里可用接口封装的


# 记录日志/失败截图  + 错误信息输出 + 抛出异常
class BasePage:
    def __init__(self, driver: WebDriver):
        # 初始化driver
        self.driver = driver

    # 1.1 等待元素可见
    def wait_ele_visible(self, loc, img_name, timeout=20, pull_fre=0.5):
        logging.info(f"等待元素{loc}可见")
        # 开始时间
        try:
            WebDriverWait(self.driver, timeout, pull_fre).until(EC.visibility_of_element_located(loc))
            # WebDriverWait(self.driver, timeout, pull_fre).until(EC.presence_of_element_located(loc))
        except:
            # 失败截图，写入日志
            self.save_screenshot(img_name)
            logging.exception("等待元素可见失败：")
            # logging.exception("等待加载失败：")
            raise
        else:
            # 等待时间结束
            pass

    # 1.2 等待元素已加载 ，适合输入框（有些输入框不可见）
    def wait_ele_present(self, loc, img_name, timeout=20, pull_fre=0.5):
        logging.info(f"等待元素{loc}已加载")
        # 开始时间
        try:
            # WebDriverWait(self.driver, timeout, pull_fre).until(EC.visibility_of_element_located(loc))
            WebDriverWait(self.driver, timeout, pull_fre).until(EC.presence_of_element_located(loc))
        except:
            # 失败截图，写入日志
            self.save_screenshot(img_name)
            # logging.exception("等待元素可见失败：")
            logging.exception("等待加载失败：")
            raise
        else:
            # 等待时间结束
            pass

    # 1.3 等待元素可点击
    def wait_ele_clickable(self, loc, img_name, timeout=20, pull_fre=0.5):
        logging.info(f"等待元素{loc}可被点击")
        # 开始时间
        try:
            WebDriverWait(self.driver, timeout, pull_fre).until(EC.element_to_be_clickable(loc))
        except:
            # 失败截图，写入日志
            self.save_screenshot(img_name)
            logging.exception("等待元素可被点击失败：")
            raise

    # 2.1查找元素
    def get_element(self, loc, img_name):
        logging.info(f"在{img_name}查找元素{loc}")
        self.wait_ele_present(loc, img_name, timeout=20, pull_fre=0.5)  # 必然的前提
        try:
            return self.driver.find_element(*loc)
        except:
            self.save_screenshot(img_name)
            logging.exception("查找元素失败")
            raise

    # 2.2查找元素集合
    def get_elements(self, loc, img_name):
        logging.info(f"在{img_name}查找元素集合{loc}")
        self.wait_ele_present(loc, img_name, timeout=20, pull_fre=0.5)  # 必然的前提
        try:
            return self.driver.find_elements(*loc)
        except:
            self.save_screenshot(img_name)
            logging.exception("查找元素集合失败")
            raise

    # 3.点击元素
    def click_element(self, loc, img_name, timeout=20, pull_fre=0.5):
        logging.info(f"在{img_name}点击元素{loc}")
        self.wait_ele_present(loc, img_name, timeout, pull_fre)  # 必然的前提
        ele = self.get_element(loc, img_name)
        try:
            ele.click()
        except:
            self.save_screenshot(img_name)
            logging.exception("点击元素失败")
            raise

    # 4.输入元素
    def input_text(self, loc, value, img_name, timeout=20, pull_fre=0.5):
        logging.info(f"在{img_name}的元素{loc}输入{value}")
        self.wait_ele_present(loc, img_name, timeout, pull_fre)  # 必然的前提
        ele = self.get_element(loc, img_name)
        try:
            ele.send_keys(value)
        except:
            self.save_screenshot(img_name)
            logging.exception("元素输入value失败")
            raise

    # 5.获取元素属性
    def get_ele_attribute(self, loc, attr_name, img_name, timeout=20, pull_fre=0.5):
        logging.info(f"在{img_name}的元素{loc}获取属性：{attr_name}")
        # 非必然的前提（元素在但不可见，也能获取到属性），去DOM对象树遍历
        self.wait_ele_present(loc, img_name, timeout, pull_fre)
        ele = self.get_element(loc, img_name)  # 必然的前提
        try:
            ele.get_attribute(attr_name)
        except:
            self.save_screenshot(img_name)
            logging.exception("获取元素的属性失败")
            raise

    # 6.获取元素文本
    def get_element_text(self, loc, img_name, timeout=20, pull_fre=0.5):
        logging.info(f"在{img_name}的元素{loc}获取文本")
        self.wait_ele_visible(loc, img_name, timeout, pull_fre)
        ele = self.get_element(loc, img_name)  # 必然的前提
        try:
            text = ele.text
            return text
        except:
            self.save_screenshot(img_name)
            logging.exception("获取元素的文本失败")
            raise

    # 7.保存截图
    def save_screenshot(self, img_name):
        """
        :param img_name: {页面名称_页面行为}
        """
        time = "1"
        file_name = f"{img_name}_{time}.png"
        self.driver.save_screenshot(file_name)
        logging.info(f"页面图片保存在{file_name}")

    # 8 iframe切换
    def switch_to_iframe(self):
        # 等待和切换一起的自带函数
        WebDriverWait(self.driver, 20).until(EC.frame_to_be_available_and_switch_to_it)
        # driver.switch_to.frame(self.frame_locator)

    # 切换新的窗口
    # alert切换
    # js执行 ，语句、参数
    # 滚动条操作
    # 上传（window？）

    # 9 获取url，也可直接用driver，因为初始化的时候一样的
    def get_url(self, url):
        self.driver.get(url)


if __name__ == '__main__':
    from selenium import webdriver

    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")
    bp = BasePage(driver)
    # 等于login_page中的self，其self就是Base类初始化时的driver对象，等效于这里的driver
    search_loc = ("id", "kw")
    bp.input_text(search_loc, "输入搜索词", "百度页面_输入操作")
