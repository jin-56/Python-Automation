from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By 

driver = webdriver.Chrome()
options = ChromeOptions()
options.add_experimental_option("detach",True)

driver =webdriver.Chrome(options=options)

driver.get("https://www.saucedemo.com/v1/")
print(driver.title)

Username = "standard_user"
Password = "secret_sauce"

username_input = driver.find_element(By.ID, "user-name")
password_input = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")

username_input.send_keys(Username)
password_input.send_keys(Password)
login_button.click()

items = driver.find_elements(By.CLASS_NAME, "inventory_item")
for item in items:
    title = item.find_element(By.CLASS_NAME, "inventory_item_name")
    print(title.text)
    if "t-shirt" in title.text.lower():
        add_cart_button = item.find_element(By.CSS_SELECTOR,"#inventory_container > div > div > div.pricebar > button")
        add_cart_button.click()
        
cart = driver.find_element(By.CSS_SELECTOR,"#shopping_cart_container > a > svg > path") 
cart.click()

check_out = driver.find_element(By.CSS_SELECTOR,"#cart_contents_container > div > div.cart_footer > a.btn_action.checkout_button")
check_out.click()

Firstname =driver.find_element(By.CSS_SELECTOR,"#first-name")
Lastname =driver.find_element(By.CSS_SELECTOR,"#last-name")
Zipcode =driver.find_element(By.CSS_SELECTOR,"#postal-code")

Firstname.send_keys("JIN")
Lastname.send_keys("MAH")
Zipcode.send_keys("600")

continue_button= driver.find_element(By.CSS_SELECTOR,"#checkout_info_container > div > form > div.checkout_buttons > input")
continue_button.click()

finish_button = driver.find_element(By.CSS_SELECTOR,"#checkout_summary_container > div > div.summary_info > div.cart_footer > a.btn_action.cart_button")
finish_button.click()

