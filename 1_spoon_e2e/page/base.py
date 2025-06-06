import time
from appium.webdriver.common.appiumby import AppiumBy

# 스크롤다운
def scroll_down(driver):
    driver.find_element(
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiScrollable(new UiSelector().scrollable(true)).scrollForward()')
    time.sleep(1)
    
# 좋아요 수 가져오기
def get_like_count(driver):
    count_text = driver.find_element(
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("co.spoonme:id/tv_like_count")'
    ).text
    return int(count_text.replace(",", ""))