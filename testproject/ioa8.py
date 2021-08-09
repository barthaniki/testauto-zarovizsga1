import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

url = "https://black-moss-0a0440e03.azurestaticapps.net/ioa8.html"
driver.get(url)

# find elements
num_1 = driver.find_element_by_id("num1").text
num_2 = driver.find_element_by_id("num2").text
op = driver.find_element_by_id("op").text
submit_btn = driver.find_element_by_id("submit")

# calculate inner result

my_result = eval(num_1 + op + num_2)

# calculate app's result

submit_btn.click()
time.sleep(2)

# check inner result with app's result

result = driver.find_element_by_id("result")
assert int(result.text) == int(my_result)

driver.close()
driver.quit()
