import json
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time


FILENAME = 'core_items'
MIN_ITEMS_COUNT = 2000

COUNT = 0


chrome_options = webdriver.ChromeOptions()
browser = webdriver.Chrome()
browser.get('https://www.thepaper.cn/')
time.sleep(0.5)
print("Woke up after 3 sec for loading index page.")
browser.find_element_by_id("hdshowsearch").click()
time.sleep(1)
print("Woke up after 3 sec.")
input_text = browser.find_element_by_id("hds_inp").send_keys("新冠疫情")
browser.find_element_by_id("search_key").click()
while True:
	COUNT += 1
	browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")
	time.sleep(5)
	length = browser.execute_script("return $('#mainContent').children().length")
	print("Scrolling on pageidx=" + str(COUNT) + "   Totally count: ", length)
	if length > 2000:
		print("Mission finished normally. Good luck!")
		break

all_results = browser.page_source

with open(FILENAME + '.html', 'a') as f:
	f.write(all_results)
	print("Saced at " + FILENAME + ".html .")


browser.close()
browser.quit()

