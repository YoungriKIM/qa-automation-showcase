def test_launch_app(driver):
    assert driver.is_app_installed("co.spoonme")
