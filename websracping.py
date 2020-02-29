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
			<li class="items"><a href=#>Item 1</a></li>
			<li class="items"><a href=#>Item 2</a></li>
			<li class="items"><a href=#>Item 3</a></li>
			<li class="items"><a href=#>Item 4</a></li>
			<li class="items"><a href=#>Item 5</a></li>
		</ul>
	</div>
</body>
</html?
"""

soup = BeautifulSoup(html_doc, 'html.parser')

#Direct
print(soup.body)