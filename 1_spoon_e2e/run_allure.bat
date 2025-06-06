@echo off
rmdir /s /q allure-results
mkdir allure-results
pytest tests/ --alluredir=allure-results

allure serve --clean allure-results

@REM allure generate allure-results --clean -o allure-report
@REM start "" "allure-report\index.html"
