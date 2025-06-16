# 선택 삭제: 삭제 기능 동작 여부

import allure
# 유틸함수, 페이지 오브젝트 불러오기
from page.cart_page import CartPage
from page.base import wait, close_alarm_modals

@allure.title("선택 삭제: 삭제 기능 동작 여부")
def test_cart_delete(driver):
    cartpage = CartPage(driver)
    
    cartpage.del_1_1_item()
    total_cart_quantity = cartpage.get_total_cart_quantity()
    
    assert total_cart_quantity == 2
