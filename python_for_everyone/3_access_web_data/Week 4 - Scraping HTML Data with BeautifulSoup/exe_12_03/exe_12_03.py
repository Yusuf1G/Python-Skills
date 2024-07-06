import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
no_of_loops = int(input('Enter Count: '))
position = int(input('Enter Position: '))

for i in range(no_of_loops):
	html = urllib.request.urlopen(url, context=ctx).read()
	soup = BeautifulSoup(html, 'html.parser')

	
	tags = soup('a')

	
	if len(tags) < position:
		print("Not enough links on the page.")
		break

	
	url = tags[position - 1].get('href', None)

	print("Last URL:", url)                      