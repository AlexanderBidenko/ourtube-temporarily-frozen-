import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import sys
sys.stdout = open('file.txt', 'w')
print('test')


options = webdriver.ChromeOptions()
options.add_argument('--window-position=5000,5000')

browser = webdriver.Chrome(options=options)

# start selenium

browser.get('https://www.youtube.com/watch?v=G0aekmshR4A')

time.sleep(5)

element1 = WebDriverWait(browser, 20).until(EC.visibility_of_all_elements_located((By.XPATH, "//ytd-menu-renderer[@class='style-scope ytd-video-primary-info-renderer']//yt-icon[@class='style-scope ytd-menu-renderer']")))

block1 = browser.find_element(By.XPATH, "//ytd-menu-renderer[@class='style-scope ytd-video-primary-info-renderer']//yt-icon[@class='style-scope ytd-menu-renderer']")

block1.click()

element2 = WebDriverWait(browser, 20).until(EC.visibility_of_all_elements_located((By.XPATH, "//ytd-menu-service-item-renderer[@class='style-scope ytd-menu-popup-renderer']//tp-yt-paper-item[@role='option']")))
block2 = browser.find_element(By.XPATH, "//ytd-menu-service-item-renderer[@class='style-scope ytd-menu-popup-renderer']//tp-yt-paper-item[@role='option']")
block2.click()
list_of_trunscription = browser.find_elements(By.XPATH, "//body/ytd-app/div[@id='content']/ytd-page-manager[@id='page-manager']/ytd-watch-flexy[@role='main']/div[@id='columns']/div[@id='secondary']/div[@id='secondary-inner']/div[@id='panels']/ytd-engagement-panel-section-list-renderer[1]/div[2]")



for i in range(len(list_of_trunscription)):
    print(list_of_trunscription[i].text)

browser.quit()
