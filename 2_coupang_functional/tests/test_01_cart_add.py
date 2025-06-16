# 장바구니 담기: 상품 장바구니에 정상 추가 여부

import allure
# 유틸함수, 페이지 오브젝트 불러오기
from page.home_page import HomePage
from page.cart_page import CartPage
from page.base import wait, close_alarm_modals

@allure.title("장바구니 담기: 상품 장바구니에 정상 추가 여부")
def test_cart_add(driver):
    homepage = HomePage(driver)
    cartpage = CartPage(driver)
    
    close_alarm_modals(driver)
    homepage.go_to_1row_index_item(1)
    homepage.go_to_1row_index_item(2)
    homepage.go_to_1row_index_item(3)
    homepage.go_to_cart()
    wait(2, "장바구니 진입 대기")
    total_cart_quantity = cartpage.get_total_cart_quantity()
    
    assert total_cart_quantity == 3
    