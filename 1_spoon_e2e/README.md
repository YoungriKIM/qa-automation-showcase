# 스푼라디오 E2E 테스트

이 테스트는 스푼라디오 앱에서 라이브 콘텐츠 진입, 채팅 메시지 전송, 좋아요 기능의 정상 동작을 검증합니다.

---

## 주요 기술 스택
- Appium + Python
- Pytest
- Page Object Pattern
- Allure 리포트

## 테스트 시나리오 요약
1. 로딩 완료 후 상위 라이브 콘텐츠에 진입
2. 채팅 버튼 클릭 → 메시지 전송
3. 메시지 전송 확인
4. 좋아요 버튼 클릭 전/후 카운트 비교

## 실행 방법
1. Android 에뮬레이터 또는 실제 디바이스 실행
2. 아래 배치 파일 실행

```bash
run_allure.bat
````

---

## 📁 폴더 구조

````
    qa-automation-showcase/
    ├── 1_spoon_e2e/ # 스푼라디오 E2E 테스트
    │ ├── tests/ # 테스트 스크립트
    │ ├── pages/ # 유틸, Page Object 정의
    │ ├── data/ # 테스트 데이터
    │ ├── conftest.py # Pytest 설정
    │ └── requirements.txt # 의존성 패키지
````