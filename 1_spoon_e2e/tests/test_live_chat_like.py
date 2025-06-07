# 유틸함수, 페이지 오브젝트
from page.live_page import LivePage
# ---------------------------------------------------------

def test_live_chat_and_like_flow(driver):
    page = LivePage(driver)
    
    page.wait_for_loading_to_finish()
    page.enter_top_live()
    page.open_chat_and_send("ㅎㅎ")
    page.verify_chat_sent("2ovlq0p")
    page.click_like_button()
