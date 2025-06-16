# 공통 유틸 (모달 닫기, 대기, 장바구니 담기)

import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException

# ----------------------------------------------------------------------------------------------
# 모달 닫기
def close_alarm_modals(driver):
    """
    쿠팡 앱 실행 시 뜨는 알림/쿠폰 등의 모달을 닫기 위한 함수, 배경을 터치해서 닫기
    """
    tried = False
    
    # outside 클릭해서 닫기
    try:
        # 배경 레이어가 있는지 확인하고 클릭
        overlay = driver.find_element(AppiumBy.ID, "com.coupang.mobile:id/touch_outside")
        overlay.click()
        print("모달 배경 클릭으로 닫기 성공")
    except NoSuchElementException:
        pass

    # ACCESSIBILITY_ID로 누르기
    try:
        close_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Close Button")
        close_btn.click()
        print("ACCESSIBILITY_ID로로 닫음")
        tried = True
    except NoSuchElementException:
        pass
    
    # ID로 누르기
    try:
        close_btn = driver.find_element(AppiumBy.ID, "com.coupang.mobile:id/close_button")
        close_btn.click()
        print("ID로 닫음")
        tried = True
    except NoSuchElementException:
        pass

    if not tried:
        print("닫을 수 있는 모달이 없음")
        
# ----------------------------------------------------------------------------------------------
# 대기 함수
def wait(seconds=3, message=None):
    """지정한 초만큼 대기하고 메시지 출력"""
    if message:
        print(f"{message} ({seconds}초)")
    time.sleep(seconds)

# ----------------------------------------------------------------------------------------------
def add_to_cart(driver):
    """
    상품 상세 페이지에서 장바구니 담기 버튼을 클릭하는 함수
    XPath와 ID 방식 모두 시도하고 담았으면 뒤로가기
    """
    tried = False

    # 1. XPath로 장바구니 버튼 찾기
    try:
        basket = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.coupang.mobile:id/text_view" and @text="장바구니 담기"]')
        basket.click()
        print("XPath 기반 장바구니 담기 클릭 성공")
        wait(2, "장바구니 담기 처리 대기")
        tried = True
        driver.back() # 뒤로가기
    except NoSuchElementException:
        pass

    # 2. ID로 장바구니 버튼 찾기
    if not tried:
        try:
            basket = driver.find_element(AppiumBy.ID, 'com.coupang.mobile:id/button_on_left')
            basket.click()
            print("ID 기반 장바구니 담기 클릭 성공")
            wait(2, "장바구니 담기 처리 대기")
            tried = True
            driver.back() # 뒤로가기
        except NoSuchElementException:
            pass

    if not tried:
        print("장바구니 버튼을 찾지 못함")