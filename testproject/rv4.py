import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

url = "https://black-moss-0a0440e03.azurestaticapps.net/rv4.html"
driver.get(url)

# find elements
all_cities = driver.find_elements_by_xpath('//textarea')
random_cities = driver.find_elements_by_xpath('//*[@id="randomCities"]/li')
missing_city = driver.find_element_by_id("missingCity")
submit_btn = driver.find_element_by_id("submit")
result = driver.find_element_by_id("result")

# create lists

all_cities_list = []

with open("cities.txt", "r") as data_file:
    cities = data_file.readline().split(", ")
    all_cities_list.append(cities)

random_cities_list = []

for city in random_cities:
    random_cities_list.append(city.text)

# trials

for city in all_cities_list:
    missing_city.clear()
    missing_city.send_keys(city)
    time.sleep(1)
    submit_btn.click()

# check result

result_msg = "Nem találtad el."

assert result.text == result_msg

driver.close()
driver.quit()
