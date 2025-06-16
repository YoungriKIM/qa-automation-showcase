@echo off
:: 기존 allure-results 폴더(이전 실행 결과) 삭제
rmdir /s /q allure-results
:: 새 allure-results 폴더 생성         
mkdir allure-results
:: 테스트 실행 결과를 allure-results 폴더에 저장
pytest tests/ --alluredir=allure-results

:: 리포트를 파일 정적 저장하고 열기
allure generate allure-results --clean -o allure-report && allure open allure-report