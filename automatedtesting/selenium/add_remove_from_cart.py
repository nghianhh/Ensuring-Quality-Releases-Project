# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
import datetime


def timestamp():
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return (ts + ': \t')

# Start the browser and login with standard_user
def login(user, password):
    print(timestamp() + 'Starting the browser...')
    options = ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument('--headless')
    options.add_argument("--disable-dev-shm-using")
    options.add_argument("--remote-debugging-port=9222")
    options.binary_location = '/usr/local/bin/google-chrome'


    driver = webdriver.Chrome(options=options)
    print(timestamp() + 'Browser started successfully')
    driver.get('https://www.saucedemo.com/')
    # login
    driver.find_element(By.CSS_SELECTOR, "input[id='user-name']").send_keys(user)
    driver.find_element(By.CSS_SELECTOR, "input[id='password']").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "input[id='login-button']").click()
    print(timestamp() + 'Login with username {:s} and password {:s} successfully.'.format(user, password))
    return driver

def add_cart(driver, n_items):
    print (timestamp() +'Test: adding items to cart')
    for i in range(n_items):
        element = "a[id='item_" + str(i) + "_title_link']"
        driver.find_element(By.CSS_SELECTOR, element).click()
        driver.find_element(By.CSS_SELECTOR, "button.btn_primary.btn_inventory").click()
        product = driver.find_element(By.CSS_SELECTOR, '.inventory_details_name.large_size').text
        print(timestamp() + product + " added to shopping cart.")
        driver.find_element(By.CSS_SELECTOR, "button.inventory_details_back_button").click()
    print(timestamp() + '{:d} items are all added to shopping cart successfully.'.format(n_items))

def remove_cart(driver, n_items):
    for i in range(n_items):
        element = "a[id='item_" + str(i) + "_title_link']"
        driver.find_element(By.CSS_SELECTOR, element).click()
        driver.find_element(By.CSS_SELECTOR, "button.btn_secondary.btn_inventory").click()
        product = driver.find_element(By.CSS_SELECTOR, '.inventory_details_name.large_size').text
        print(timestamp() + product + " removed from shopping cart.")
        driver.find_element(By.CSS_SELECTOR, "button.inventory_details_back_button").click()
    print(timestamp() + '{:d} items are all removed from shopping cart successfully.'.format(n_items))

def add_cart_check(driver, n_items):
    print (timestamp() +'Test: adding items to cart for check out')
    for i in range(n_items):
        element = "a[id='item_" + str(i) + "_title_link']"
        driver.find_element(By.CSS_SELECTOR, element).click()
        driver.find_element(By.CSS_SELECTOR, "button.btn_primary.btn_inventory").click()
        product = driver.find_element(By.CSS_SELECTOR, '.inventory_details_name.large_size').text
        print(timestamp() + product + " added to shopping cart.")
        driver.find_element(By.CSS_SELECTOR, "button.inventory_details_back_button").click()
    print(timestamp() + '{:d} items are all added to shopping cart successfully ready checkout.'.format(n_items))

def check_out(driver):
    driver.get('https://www.saucedemo.com/inventory.html')
    driver.find_element(By.CSS_SELECTOR, '.shopping_cart_badge').click()
    driver.find_element(By.CSS_SELECTOR, '#checkout').click()
    driver.find_element(By.CSS_SELECTOR, "input[id='first-name']").send_keys('Anh')
    driver.find_element(By.CSS_SELECTOR, "input[id='last-name']").send_keys('Pham')
    driver.find_element(By.CSS_SELECTOR, "input[id='postal-code']").send_keys('11111')
    driver.find_element(By.CSS_SELECTOR, '#continue').click()
    driver.find_element(By.CSS_SELECTOR, '#finish').click()
    status_check = driver.find_element(By.CSS_SELECTOR, '.complete-header').text
    print(timestamp() + status_check + " .Your order has been dispatched, and will arrive just as fast as the pony can get there!")
    driver.find_element(By.CSS_SELECTOR, '#back-to-products').click()

if __name__ == "__main__":
    driver = login('standard_user', 'secret_sauce')
    add_cart(driver, 3)
    remove_cart(driver, 3)
    add_cart_check(driver, 3)
    check_out(driver)
    print(timestamp() + 'Selenium tests are all successfully completed!')
