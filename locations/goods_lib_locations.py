from selenium.webdriver.common.by import By


class GoodsLibLocations:
    # 进入商品库
    goods_lib = (By.XPATH, '//li//span[text()="商品库"]')
    # 或者直接访问商品库的url：https://sale.favokit.com/oem/goodsLib?mallCode=Ma6qnw00igemf

    # 搜索-商品名称或ID
    searchKey = (By.XPATH, '//input[@id="searchKey"]')
    # 搜索-商品编码
    sellerDefinedCode = (By.XPATH, '//input[@id="sellerDefinedCode"]')
    # 搜索-商品类目
    categoryLevel = (By.XPATH, '//input[@id="categoryLevel"]')
    # 搜索-商品PID
    pid = (By.XPATH, '//input[@id="pid"]')
    # 查询的按钮
    search = (By.XPATH, '//button[text()="查询"]')
    # 清空筛选条件的按钮
    clear_condition = (By.XPATH, '//button[text()="清空筛选条件"]')
