# 홈 화면 관련 기능

# 라이브러리 호출
from appium.webdriver.common.appiumby import AppiumBy

# 유틸함수, 페이지 오브젝트
from page.base import wait, add_to_cart

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        
    def go_to_1row_index_item(self, index):
        """주목할 상품 index 번째 페이지 진입"""
        top_1_item_xpath = f'//android.widget.FrameLayout[@resource-id="com.coupang.mobile:id/dcoContainer"]/android.widget.LinearLayout/android.widget.GridView/android.widget.FrameLayout[{index}]/android.widget.LinearLayout/android.widget.ImageView'
        top_1_item = self.driver.find_element(AppiumBy.XPATH, top_1_item_xpath)
        top_1_item.click()
        wait(2, f"1-{index}번째 상품 상세 진입 대기")
        # 장바구니 담기
        add_to_cart(self.driver)
        self.driver.back()
    
    def go_to_cart(self):
        """장바구니 담기"""
        cart_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "장바구니")
        cart_button.click()
        wait(2, "장바구니 진입 대기")
    
    
    