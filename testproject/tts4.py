from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

url = "https://black-moss-0a0440e03.azurestaticapps.net/tts4.html"
driver.get(url)

# find elements
submit_btn = driver.find_element_by_id("submit")

# money tossing 100 times
for _ in range(100):
    submit_btn.click()

# collect "fej" results
res_list = []

results = driver.find_elements_by_xpath('//*[@id="results"]/li')

for result in results:
    if result.text == "fej":
        res_list.append(result.text)

# check that "fej" results are at least 30
assert len(res_list) >= 30

driver.close()
driver.quit()
