# 유틸함수, 페이지 오브젝트 불러오기
from page.live_page import LivePage

# ---------------------------------------------------------
# E2E 흐름

def test_live_chat_and_like_flow(driver):
    page = LivePage(driver)
    
    # 앱 접속 → Top Lives 첫 번째 접속 → 채팅 입력, 전송  → 채팅 전송 확인 → 좋아요 버튼 활성화 대기 → 좋아요 전송 → 좋아요 개수 확인 → 마무리
    page.wait_for_loading_to_finish()
    page.enter_top_live()
    page.open_chat_and_send("ㅎㅎ")
    page.verify_chat_sent("2ovlq0p")
    page.click_like_button()
