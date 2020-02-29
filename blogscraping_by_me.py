import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get('https://www.ineedcopy.com/blog/')
soup = BeautifulSoup(response.text, 'html.parser')
posts = soup.find_all(class_='awr h-me')

with open('posts.csv', 'w') as csv_file:
	csv_writer = writer(csv_file)
	headers = ['title', 'link', 'date']
	csv_writer.writerow(headers)
	for post in posts:
		title = post.find(class_='entry-title').get_text().replace('\n', '')
		link = post.find('a')['href']
		date = post.find(class_='meta').get_text()
		csv_writer.writerow([title, link, date])