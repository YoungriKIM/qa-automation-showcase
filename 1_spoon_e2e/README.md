# 스푼라디오 E2E 테스트

[▶ 시연 영상 보기](https://youtu.be/eCFZxZh4KGQ)

[![시연 영상 썸네일](https://img.youtube.com/vi/eCFZxZh4KGQ/0.jpg)](https://youtu.be/eCFZxZh4KGQ)

이 테스트는 스푼라디오 앱에서 실사용자가 가장 자주 사용하는 핵심 기능 3가지를 자동화 테스트로 검증하였습니다.
- 라이브 콘텐츠 진입
- 채팅 전송
- 좋아요 기능

---
<br>

### 테스트 흐름

| 단계 | 수행 내용 | 목적 |
|------|-----------|------|
| 1 | 앱 실행 및 로딩 완료 대기 | 테스트 시작 준비 |
| 2 | Top Lives 첫 번째 콘텐츠 진입 | 대표 콘텐츠 선택 및 진입 |
| 3 | 채팅 입력 및 전송 | 라이브 내 채팅 기능 동작 검증 |
| 4 | 채팅 전송 내역 확인 | 메시지 전송 여부 검증 |
| 5 | 좋아요 버튼 활성화 대기 | 좋아요 활성화 기능 검증 |
| 6 | 좋아요 클릭 | 좋아요 누적 기능 확인 |

<br><br>

### 주요 기술 스택
- Appium + Python : Android 앱 자동화
- Appium Inspector: 모바일 요소 탐색, XPath 추출
- Pytest : 테스트 프레임워크
- Page Object Pattern : 유지보수를 고려한 테스트 구조
- Allure Report : 시각적 리포트 및 테스트 기록

<br><br>

### 실행 방법
1. 사전 준비
     - Android 에뮬레이터 실행
     - Appium 서버 실행
     - 스푼라디오 APK 설치 (공식 앱스토어 또는 테스트용 APK 사용)
     - 테스트용 계정 로그인

2. 테스트 실행
     - 아래 배치 파일 실행
       ```bash
       # Windows 환경에서 실행
       run_allure.bat
       ```

<br><br>

### 테스트 리포트 요약
- 테스트는 정상적으로 통과되었으며, 전체 흐름은 다음과 같이 검증되었습니다.
- 총 1개 실시간 시나리오 자동화 완료 / 채팅 및 좋아요 기능 정상 동작 / UI 플로우 이상 없음 / Allure Report 기준 전 항목 통과

![테스트 리포트 요약](../assets/spoon_e2e.JPG)

<br><br>

### 📁 폴더 구조
````
qa-automation-showcase/
└── 1_spoon_e2e/ # 스푼라디오 E2E 테스트
  ├── pages/ # 유틸, Page Object 정의
  ├── tests/ # 테스트 스크립트
  ├── conftest.py # Pytest 설정
  ├── requirements.txt # 의존성 패키지
  └── run_allure.bat # 실행 배치 파일

````
<br><br>
