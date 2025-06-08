# QA Automation Showcase

자동화 테스트 실습 프로젝트입니다.  
Appium + Pytest 기반으로, 모바일 앱의 기능과 시나리오 테스트를 구성하였습니다.
1. 스푼라디오 E2E 테스트
2. 당근마켓 기능 테스트

---


### 📁 폴더 구조

````
qa-automation-showcase/
├── 1_spoon_e2e/ # 스푼라디오 E2E 테스트
├── 2_carrot_functional/ # 당근마켓 기능 테스트
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
- Android SDK: 설치 후 환경변수 `ANDROID_HOME` 설정 필요
- Android Emulator or Device: Android API Level 30 이상 권장
- 테스트 대상 APK
  - 앱 이름: Spoon: Live Audio & Podcasts
  - 버전: v10.1.0
  - 패키지명: `co.spoonme`
  - 출처: [APKPure](https://apkpure.com)에서 다운로드(⚠️APK 파일 자체는 저장소에 포함되어 있지 않습니다.)
- 기타 도구:
  - `allure-pytest`: 테스트 리포트 생성
