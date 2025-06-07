# appium 옵션 설정, 서버 연결

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

@pytest.fixture(scope="module")
# module — 파일 내 테스트가 많고 동일한 driver를 계속 사용할 때
# function — 각 테스트가 독립적으로 실행되도록 하고 싶을 때

def driver():
    options = UiAutomator2Options().load_capabilities({
        "platformName": "Android",
        "deviceName": "emulator-5554",  # ADB에서 보이는 이름을 지정
        "appPackage": "co.spoonme",     # 사용하는 APK에 맞게
        "appActivity": "co.spoonme.ui.main.MainActivity",
        "noReset": True # 앱 초기화 여부를 결정
    })
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)
    yield driver # 테스트 함수에 driver 넘겨주기
    driver.quit() # 테스트가 다 끝나면 여기에 도달, 즉 앱 종료