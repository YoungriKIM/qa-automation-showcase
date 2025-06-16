# 상품 이름 클릭: 해당 상품 페이지 연결 여부

import allure
# 유틸함수, 페이지 오브젝트 불러오기
from page.cart_page import CartPage
from page.product_page import ProductPage
from page.base import wait, close_alarm_modals

@allure.title("상품 이름 클릭: 해당 상품 페이지 연결 여부")
def test_product_detail_link(driver):
    cartpage = CartPage(driver)
    product_page = ProductPage(driver)
    
    item_1_title = cartpage.get_1_1_item_title()
    cartpage.go_to_product_page()
    product_title = product_page.get_product_title()
    
    assert item_1_title == product_title[:len(item_1_title)]