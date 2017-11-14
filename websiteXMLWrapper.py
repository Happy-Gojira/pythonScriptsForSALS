from bs4 import BeautifulSoup
data = open("systems.html", 'r').read()

soup = BeautifulSoup(data, 'html.parser')
url= []
for link in soup.find_all('a'):
	url.append(link.get('href'))
print(url[5])
x=len(url)
print(x)