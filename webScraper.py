# import libraries 
from urllib.request import urlopen 
from bs4 import BeautifulSoup
web_page = 'http://www.lib-web.org/index.php?search=system&p=201'
page = urlopen(web_page)
soup = BeautifulSoup(page, 'html.parser')
library_box = soup.find_all('a', attrs={'class':'link'})
print (library_box)
