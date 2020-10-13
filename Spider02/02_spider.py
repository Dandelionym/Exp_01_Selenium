import json
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time


FILENAME = 'content_items'
MIN_ITEMS_COUNT = 1000

COUNT = 0
WATCH = 0
SLEEP_TIME = 2.8

chrome_options = webdriver.ChromeOptions()
browser = webdriver.Chrome()
browser.get('https://www.thepaper.cn/newsDetail_forward_1543651')
content_count = browser.execute_script("return $('#comm_span').text()")
print(content_count)

while True:
	COUNT += 1
	browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")
	# time.sleep(SLEEP_TIME)
	length = browser.execute_script("return $('#mainContent').children().length")
	print("Scrolling on cont_idx=" + str(COUNT) + "   Totally count: ", length-2)
	if length >= 688:
		print("Mission finished normally. Good luck!")
		break

all_results = browser.page_source
soup = BeautifulSoup(all_results, 'html.parser')
soup = soup.find('div', id='mainContent')

with open(FILENAME + '.html', 'a') as f:
	f.write(str(soup))
	print("Saced at " + FILENAME + ".html .")

browser.close()
browser.quit()



