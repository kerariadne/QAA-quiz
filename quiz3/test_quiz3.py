from selenium import webdriver

def test_quiz3():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    page = driver.get('https://www.saucedemo.com/')
    driver.maximize_window()

    page.login("standard_user", "secret_sauce")
    assert "inventory" in driver.current_url

    error_text = page.login("invalid_user", "invalid_pass")
    assert error_text == "Epic sadface: Username and password do not match any user in this service", "Expected error message for invalid login credentials"

    page.sort_products("Price (low to high)")

    product_price = page.get_product_price()
    product_name = page.get_product_name()
    assert product_price == "$29.99", "Expected price to be $29.99"

    page.add_to_cart()
    assert page.is_remove_button_displayed(), "Expected 'Remove' button to be displayed after adding to cart"

    page.go_to_cart()
    assert page.get_product_price() == product_price, "Expected product price in cart to match"
    assert page.get_product_name() == product_name, "Expected product name to match"

    page.go_to_checkout()
    checkout_page = page(driver)
    checkout_page.continue_checkout("", "", "")
    error_message = checkout_page.get_error_message()
    assert "Error: First Name is required" in error_message, "Expected error message for missing first name"