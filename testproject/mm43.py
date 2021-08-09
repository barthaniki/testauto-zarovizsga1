import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

url = "https://black-moss-0a0440e03.azurestaticapps.net/mm43.html"
driver.get(url)

# find elements
email = driver.find_element_by_id("email")
submit_btn = driver.find_element_by_id("submit")
validation_error_msgs = driver.find_elements_by_xpath('//div[@class="validation-error"]')

# TC1: correct fill - No validation error message

test_email = "teszt@elek.hu"

email.send_keys(test_email)
submit_btn.click()
time.sleep(2)

# check no validation error message
assert len(validation_error_msgs) == 0

# TC2: incorrect email address with validation error message

test_email = "teszt@"

email.clear()
email.send_keys(test_email)
submit_btn.click()
time.sleep(2)

# check validation error message
validation_error_msg = driver.find_element_by_xpath('//div[@class="validation-error"]')

# Please enter a part following '@'. 'teszt@' is incomplete. - A tesztben magyarul!
error_msg = "Kérjük, adja meg a „@” utáni részt is. A(z) „teszt@” cím nem teljes."

assert validation_error_msg.text == error_msg

# TC3: empty input field

email.clear()
submit_btn.click()
time.sleep(2)

# check validation error message
validation_error_msg = driver.find_element_by_xpath('//div[@class="validation-error"]')

# Please fill out this field. - A tesztben magyarul!
error_msg = "Kérjük, töltse ki ezt a mezőt."

assert validation_error_msg.text == error_msg

driver.close()
driver.quit()
