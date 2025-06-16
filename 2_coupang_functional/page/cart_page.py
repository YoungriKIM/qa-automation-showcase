# 장바구니 관련 기능

# 라이브러리 호출
from appium.webdriver.common.appiumby import AppiumBy
import re

# 유틸함수, 페이지 오브젝트
from page.base import wait

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        
    def get_total_cart_quantity(self):
        """장바구니 전체에 담긴 상품 개수 가져오기 """
        purchase_btn = self.driver.find_element(AppiumBy.ID, "com.coupang.mobile:id/cart_purchase_btn")
        purchase_text = purchase_btn.text
        match = re.search(r"총\s*(\d+)\s*개", purchase_text)
        purchase_count = int(match.group(1))
        print(f"장바구니에 담긴 상품 수: {purchase_count}")
        return purchase_count
        
    def get_quantity(self):
        """단일 상품 개수 가져오기"""
        xpath = '(//android.view.ViewGroup[@resource-id="com.coupang.mobile:id/cart_item_quantity_picker"])[1]//android.widget.TextView[@resource-id="com.coupang.mobile:id/text_quantity"]'
        return int(self.driver.find_element(AppiumBy.XPATH, xpath).text)
    
    def increase_quantity(self):
        """단일 상품 개수 +1"""
        plus_button = self.driver.find_element(AppiumBy.ID, 'com.coupang.mobile:id/button_plus')
        plus_button.click()
        
    def decrease_quantity(self):
        """단일 상품 개수 -1"""
        minus_button = self.driver.find_element(AppiumBy.ID, 'com.coupang.mobile:id/button_minus')
        minus_button.click()
        
    def del_1_1_item(self):
        """장바구니 첫번째 상품 삭제"""
        item_1_del_button = self.driver.find_element(AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.coupang.mobile:id/cart_item_delete_img"])[1]')
        item_1_del_button.click()
        
    def get_1_1_item_title(self):
        """장바구니 첫번째 상품명 가져오기"""
        item_1_title = self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.coupang.mobile:id/cart_item_title"]')
        item_1_title_text = item_1_title.text
        print(f"상품명: {item_1_title_text}")
        return item_1_title_text
    
    def go_to_product_page(self):
        """장바구니 첫번째 상품 상세 페이지 이동"""
        item_1_title = self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.coupang.mobile:id/cart_item_title"]')
        item_1_title.click()
        wait(2, "페이지 진입 대기")
        
    def go_to_order_page(self):
        """주문/결제 페이지 이동"""
        purchase_btn = self.driver.find_element(AppiumBy.ID, "com.coupang.mobile:id/cart_purchase_btn")
        purchase_btn.click()
        wait(2, "페이지 진입 대기")
        
        main_title_text = self.driver.find_element(AppiumBy.ID, "com.coupang.mobile:id/text_main_title").text
        print(f"페이지 이름: {main_title_text}")
        return main_title_text