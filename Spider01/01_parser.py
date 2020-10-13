from bs4 import BeautifulSoup

with open('01_page.html', mode='r', encoding='utf-8') as F:
	html_read = F.read()
html = BeautifulSoup(html_read, "html.parser")
container = html.find_all('div', class_='search_res')  # 获取关键标签的父容器

for item in container:
	item_soup = BeautifulSoup(str(item), 'html.parser')
	title = item_soup.find('h2').find('a').text
	print(title)
