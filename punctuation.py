#http://bark.phon.ioc.ee/punctuator
#try to

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


options = webdriver.ChromeOptions()

browser = webdriver.Chrome(options=options)

# start selenium

concotinatestr = "some text for example it s time to say hello world"
browser.get('http://bark.phon.ioc.ee/punctuator')

time.sleep(1)


block1 = browser.find_element(By.XPATH, "//html[1]/body[1]/div[1]/div[2]/div[1]/textarea[1]")
block1.send_keys(concotinatestr)



block2 = browser.find_element(By.ID, "punctuate-btn")
block2.click()
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
element2 = WebDriverWait(browser, 20).until(EC.visibility_of_all_elements_located((By.ID, "output-text")))
punctuation_str = browser.find_element(By.ID, "output-text").text

p_str = punctuation_str


print(p_str)

print(type(p_str))

print(p_str)


browser.quit()
