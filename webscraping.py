from bs4 import BeautifulSoup

html_doc = """
<!DOCTYPE html>
<html lanf="en">
<head>
	<meta charset="UFT-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title>MYwebpage</title>
</head>
<body>
	<div id="section-1">
	<h3 data-hello="hi">Hello</h3>
	<img src="https://unsplash.com/photos/FkkUuSDQ_KI" />
	<p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged</p>
	</div>
	<div id="section-2">
		<ul class="items">
			<li class="item"><a href=#>Item 1</a></li>
			<li class="item"><a href=#>Item 2</a></li>
			<li class="item"><a href=#>Item 3</a></li>
			<li class="item"><a href=#>Item 4</a></li>
			<li class="item"><a href=#>Item 5</a></li>
		</ul>
	</div>
</body>
</html?
"""

soup = BeautifulSoup(html_doc, 'html.parser')

#Direct
#print(soup.body)
#print(soup.head)
#print(soup.head.title)

#find()

#el = soup.find('div')

#find_all(), findAll()
#el = soup.find_all('div')
#el = soup.find_all('div')[1]
#el = soup.find(id='section-1')
#el = soup.find(class_='items')
#el = soup.find(attrs={"data-hello": "hi"})
#select
#el = soup.select('#section-1')
#el = soup.select('#section-1')[0]
#el = soup.select('.item')[3]

#get_text()
#el = soup.find(class_='item').get_text()

#for loop
#for item in soup.select('.item'):
#	print(item.get_text())
#Navigation
#el = soup.body.contents
#el = soup.body.contents[1]
#el = soup.body.contents[1].contents[1]
#to find sibling
#el = soup.body.contents[1].contents[1].next_sibling.next_sibling
#el = soup.body.contents[1].contents[1].find_next_sibling()
#el = soup.find(id='section-2').find_previous_sibling()
#el = soup.find(class_='item').find_parent()
#el = soup.find('h3').find_next_sibling('p')


print(el)
