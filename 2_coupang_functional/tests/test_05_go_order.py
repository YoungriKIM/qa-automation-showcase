# 하단 "총 N개 상품 구매하기" 클릭: 주문 페이지로 이동 여부

import allure
# 유틸함수, 페이지 오브젝트 불러오기
from page.cart_page import CartPage

@allure.title('하단 "총 N개 상품 구매하기" 클릭: 주문 페이지로 이동 여부')
def test_go_order(driver):
    cartpage = CartPage(driver)

    driver.back()
    order_title = cartpage.go_to_order_page()
    
    assert order_title == "주문/결제"