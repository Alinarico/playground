from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Firefox()
browser.get('https://www.saucedemo.com')

wait = WebDriverWait(browser, 10)

user_name_input = browser.find_element(By.ID, "user-name")
user_name_input.send_keys("standard_user")

password_input = browser.find_element(By.ID, "password")
password_input.send_keys("secret_sauce")

login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#login-button")))
login_button.click()

product_title = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))
assert product_title.is_displayed()
assert product_title.text == "PRODUCTS"

hamburger_button = wait.until(EC.element_to_be_clickable((By.ID, "react-burger-menu-btn")))
hamburger_button.click()

log_out_button = wait.until(
   EC.element_to_be_clickable((
      By.CSS_SELECTOR, "#logout_sidebar_link")
   ))
log_out_button.click()

login_button = browser.find_element(
   By.CSS_SELECTOR, "#login-button"
)
assert login_button.is_displayed()

user_name_input = browser.find_element(By.ID, "user-name")
user_name_input.send_keys("locked_out_user")

password_input = browser.find_element(By.ID, "password")
password_input.send_keys("secret_sauce")

login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#login-button")))
login_button.click()

error_box = wait.until(
   EC.text_to_be_present_in_element(
      (By.CSS_SELECTOR, ".error-message-container"),
      "Epic sadface: Sorry, this user has been locked out.")
)

browser.close()