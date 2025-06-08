@echo off
:: 기존 allure-results 폴더(이전 실행 결과) 삭제
rmdir /s /q allure-results
:: 새 allure-results 폴더 생성         
mkdir allure-results
:: 테스트 실행 결과를 allure-results 폴더에 저장
pytest tests/ --alluredir=allure-results

:: 테스트 후 리포트 뷰어 실행 시(브라우저로 리포트 자동 오픈)
allure serve --clean allure-results

:: 리포트를 파일 정적 저장, 수동으로 열기 시
@REM allure generate allure-results --clean -o allure-report
@REM allure serve allure-results