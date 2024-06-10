from selenium.webdriver.common.by import By

class Locators:
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    SORT_SELECT = (By.CLASS_NAME, "product_sort_container")
    ADD_TO_CART_BUTTON = (By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/button")
    REMOVE_BUTTON = (By.XPATH, '//*[@id="remove-sauce-labs-backpack"]')
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    PRODUCT_PRICE = (By.CLASS_NAME, "inventory_item_price")
    PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    ERROR_MESSAGE = (By.CLASS_NAME, "error-message-container")