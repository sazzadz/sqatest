from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
browser = webdriver.Chrome("C:\Program Files\chromedriver.exe")
browser.maximize_window()

browser.get('https://www.youtube.com/watch?v=vzXdnYJNZDw')
time.sleep(7)
browser.find_element_by_id("video-title").click()
