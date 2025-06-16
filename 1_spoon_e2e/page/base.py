# 공통 유틸 (스크롤, 텍스트 등)

import time
from appium.webdriver.common.appiumby import AppiumBy

# ----------------------------------------------------------------------------------------------
def scroll_down(driver):
    """스크롤 다운하여 다음 콘텐츠 보기"""
    driver.find_element(
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiScrollable(new UiSelector().scrollable(true)).scrollForward()')
    time.sleep(1)

# ----------------------------------------------------------------------------------------------
def get_like_count(driver):
    """좋아요 수를 텍스트에서 추출"""
    count_text = driver.find_element(
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("co.spoonme:id/tv_like_count")'
    ).text
    return int(count_text.replace(",", ""))