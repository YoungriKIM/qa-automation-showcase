# QA Automation Showcase

자동화 테스트 실습 프로젝트입니다.  
Appium + Pytest 기반으로, 모바일 앱의 기능과 시나리오 테스트를 구성하였습니다.   
각 서비스별 테스트 정보, 테스트 코드는 각 폴더 내 README.md에서 확인하실 수 있습니다.  

1. 스푼라디오 E2E 테스트
   - 실시간 콘텐츠 진입, 채팅, 좋아요 등 실사용 중심의 흐름을 전체 자동화
   - 사용자 인터랙션 기능 검증에 초점

2. 쿠팡 장바구니 기능 테스트
   - 상품 담기, 수량 변경, 삭제, 상세 페이지 진입 등 장바구니 관련 주요 기능 분리 테스트
   - 기능 단위별 동작 검증 및 UI 반응 확인

<br>

---

### 📁 폴더 구조

````
qa-automation-showcase/
├── 1_spoon_e2e/ # 스푼라디오 E2E 테스트
├── 2_coupang_functional/ # 쿠팡 장바구니 기능 테스트
└── assets/ # 시연 영상
````

### ✅ 실행 환경 정보

- 운영체제: Windows 10
- Python: 3.11.13
- Java JDK: 1.8.0_202
- Node.js: 18.15.0
- npm: 9.5.0
- Appium: 2.19.0
- ADB (Android Debug Bridge): 1.0.41 (v35.0.2-12147458)
- Android SDK: 설치 후 환경변수 `ANDROID_HOME`, `PATH` 설정 필요
- Android Emulator or Device: Android API Level 30 이상 권장
- 테스트 대상 APK (APK 파일 자체는 저장소에 포함되어 있지 않습니다.)
  - 스푼라디오: Spoon: Live Audio & Podcasts
    - 패키지명: `co.spoonme` 
  - 쿠팡: 쿠팡 (Coupang)
    - 패키지명: `com.coupang.mobile`
- 기타 도구:
  - `allure-pytest`: 테스트 리포트 생성
