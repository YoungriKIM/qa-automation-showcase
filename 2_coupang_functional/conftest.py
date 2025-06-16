# appium 옵션 설정, 서버 연결

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

@pytest.fixture(scope="session")
# module — 테스트 함수마다 새로 실행 / 테스트가 서로 완전히 독립적일 때 (초기화 필요)
# function — 테스트 파일마다 1회 실행 / 하나의 파일 안에서만 상태 유지하고 싶을 때
# session — 전체 테스트 세션 동안 1회 실행 / 여러 테스트 파일 간 앱 상태를 유지하고 싶을 때

def driver():
    options = UiAutomator2Options().load_capabilities({
        "platformName": "Android",
        "deviceName": "emulator-5554",  # ADB에서 보이는 이름을 지정
        "appPackage": "com.coupang.mobile",     # 사용하는 APK에 맞게
        "appActivity": "com.coupang.mobile.domain.home.presentation.view.MainActivity",
        "noReset": True # 앱 초기화 여부를 결정
    })
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)
    yield driver # 테스트 함수에 driver 넘겨주기
    driver.quit() # 테스트가 다 끝나면 여기에 도달, 즉 앱 종료