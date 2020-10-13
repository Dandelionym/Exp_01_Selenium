from bs4 import BeautifulSoup


with open(file='./02_text.html', mode='r', encoding='utf-8') as F:
	content = F.read()

html = BeautifulSoup(content, "html.parser")
container = html.find_all('div', class_='comment_que')  # 获取关键标签的父容器

item_dict = {}
all_item_lst = []

for item in container:
	item_soup = BeautifulSoup(str(item), 'html.parser')
	user  = item_soup.find('h3').find('a').text
	dtime = item_soup.find('span').text
	content = item_soup.find('div', class_='ansright_cont').text
	sugg = item_soup.find('a', class_='ansright_zan').text
	item_dict['user'] = user
	item_dict['dtime'] = dtime
	item_dict['content'] = content
	item_dict['sugg'] = sugg
	all_item_lst.append(item_dict)
	item_dict = {}


for i in all_item_lst:
	print(i)
	
