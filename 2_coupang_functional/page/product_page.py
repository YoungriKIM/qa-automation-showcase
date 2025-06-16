# 상품 상세 화면 관련 기능

# 라이브러리 호출
from appium.webdriver.common.appiumby import AppiumBy

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        
    def get_product_title(self):
        """상세 페이지 상품명 가져오기"""
        page_title = self.driver.find_element(AppiumBy.ID, "com.coupang.mobile:id/name_text")
        page_title_text = page_title.text
        print(f"상품명: {page_title_text}")
        return page_title_text