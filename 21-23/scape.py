import requests
from bs4 import BeautifulSoup

base_url = "https://www.yelp.com/search?find_desc=Restaurants&find_loc="
loc = 'Newport+Beach,+CA'
page = 10

url = base_url + loc + "&start" + str(page)

yelp_r = requests.get(url)
yelp_soup = BeautifulSoup(yelp_r.text, 'html.parser')
print(yelp_soup.prettify())

business = yelp_soup.findAll('div', {'class':'businessName__373c0__1fTgn'})

for biz in business:
	#print(biz.text)
	title = biz.findAll('a', {'class':'link__373c0__29943'})[0].text
	print(title)
	address = biz.findAll('address')[0]
	print(address)
	print('\n')
	phone = biz.findAll('span', {'class': 'display--inline-block__373c0__2de_K'})[0].text
	print(phone)
 
file_path = 'yelp-{loc}.txt'.format(loc=loc)
with open(file_path, "a") as textfile:
	business = yelp_soup.findAll('div', {'class': 'businessName__373c0__1fTgn'})
	for biz in business:
		#print(biz.text)
		title = biz.findAll('a', {'class': 'link__373c0__29943'})[0].text
		print(title)
		address = biz.findAll('address')[0]
		print(address)
		print('\n')
		phone = biz.findAll('span', {'class': 'display--inline-block__373c0__2de_K'})[0].text
		print(phone)
		page_line = "{title}\n{address}\n{phone}\n\n".format(
				title = title,
				address = address,
				phone = phone
			)
		textfile.write(page_line)





print(yelp_soup.findAll('li',{'class_':'list-item__373c0__M7vhU'}))

print(yelp_soup.findAll('a',{'class_':'link__373c0__29943'}))


for name in yelp_soup.findAll('a',{'class_':'link__373c0__29943'}):
	print(name.text)























print(yelp_r.status_code)


yelp_soup = BeautifulSoup(yelp_r.text, 'html.parser')

print(yelp_soup.prettify())

print(yelp_soup.findAll('a'))


for link in yelp_soup.findAll('a'):
	print(link)