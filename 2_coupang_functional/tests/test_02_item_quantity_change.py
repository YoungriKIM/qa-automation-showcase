# 수량 조절(+-): 수량 변경 정상 여부

import allure
# 유틸함수, 페이지 오브젝트 불러오기
from page.cart_page import CartPage

@allure.title("수량 조절(+-): 수량 변경 정상 여부")
def test_item_quantity(driver):
    cartpage = CartPage(driver)
    
    cartpage.increase_quantity()
    item_1_1_quantity = cartpage.get_quantity()
    assert item_1_1_quantity == 2
    
    cartpage.decrease_quantity()
    item_1_1_quantity = cartpage.get_quantity()
    assert item_1_1_quantity == 1
