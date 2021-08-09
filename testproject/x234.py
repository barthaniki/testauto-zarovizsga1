import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

url = "https://black-moss-0a0440e03.azurestaticapps.net/x234.html"
driver.get(url)

# find elements
input_a = driver.find_element_by_id("a")
input_b = driver.find_element_by_id("b")
submit_btn = driver.find_element_by_id("submit")
result = driver.find_element_by_id("result")


def calc(a, b):
    input_a.clear()
    input_a.send_keys(a)
    input_b.clear()
    input_b.send_keys(b)
    submit_btn.click()
    time.sleep(1)


# TC1: correct fill
a = 99
b = 12
result_1 = "222"

calc(a, b)

assert result.text == result_1

# TC2: fill with not numbers
a = "kiskutya"
b = "12"
result_2 = "NaN"

calc(a, b)

assert result.text == result_2

# TC3: blank fill
a = ""
b = ""
result_3 = "NaN"

calc(a, b)

assert result.text == result_3

driver.close()
driver.quit()
