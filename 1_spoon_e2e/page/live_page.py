# 라이브 화면 요소와 동작 정의

# 라이브러리 호출
import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

# 유틸함수, 페이지 오브젝트
from page.base import scroll_down, get_like_count

class LivePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("앱 접속 후 로딩바가 사라질 때까지 대기")
    def wait_for_loading_to_finish(self):
        WebDriverWait(self.driver, 20).until( # 최대 20초까지
            EC.invisibility_of_element_located(( # 사라질 때까지
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().className("android.widget.ProgressBar")'
            ))
        )

    @allure.step("Content Rank 중 첫 번째 라이브 클릭")
    def enter_top_live(self):
        for _ in range(5):
            try:
                top_1_rank = self.driver.find_element(
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().description("Content Rank").instance(0)'
                )
                break
            except:
                scroll_down(self.driver)
        assert top_1_rank is not None, "Top Lives 1번 보이지 않음"
        top_1_rank.click() # 방송 진입
        
    def open_chat_and_send(self, message):
        with allure.step("채팅 버튼 클릭"):
            chat_btn = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((
                    AppiumBy.ACCESSIBILITY_ID, "chat button"
                ))
            )
            assert chat_btn is not None, "채팅 버튼 찾을 수 없음"
            chat_btn.click()

        with allure.step("채팅 입력창에 메시지 입력"):
            input_box = self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().className("android.widget.EditText")'
            )
            assert input_box is not None, "채팅 입력창 찾을 수 없음"
            input_box.send_keys(message)
        
        with allure.step("채팅 보내기 버튼 클릭"):
            send_btn = self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().text("Send")'
            )
            assert send_btn is not None, "보내기 버튼 찾을 수 없음"
            send_btn.click()

    @allure.step("화면에 로그인 한 유저 아이디가 나타나는지 확인")
    def verify_chat_sent(self, user_id):
        self.driver.back()  # 채팅창 닫기
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((
                AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiSelector().text("{user_id}")'
            ))
        )

    def click_like_button(self):
        with allure.step("좋아요 버튼 활성화 후 클릭(처음에 1분 필요)"):
            timeout, check_interval = 60, 5
            start_time = time.time()
            like_enabled  = False
            while time.time() - start_time < timeout:
                try:
                    self.driver.find_element(
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().resourceId("co.spoonme:id/v_dot")'
                    )
                    like_enabled = True
                    break
                except:
                    time.sleep(check_interval) # 5초 대기
            assert like_enabled, "1분 내 좋아요 버튼 활성화 안 됨"

        with allure.step("좋아요 누른 후 좋아요 개수 증가 확인"):
            initial_likes = get_like_count(self.driver)
            self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().resourceId("co.spoonme:id/iv_heart")'
            ).click()
            time.sleep(2)
            updated_likes = get_like_count(self.driver)
            assert updated_likes > initial_likes, "좋아요 수 증가 안 됨"