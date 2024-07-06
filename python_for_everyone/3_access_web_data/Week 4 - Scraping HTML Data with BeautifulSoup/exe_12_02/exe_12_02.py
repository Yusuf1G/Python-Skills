from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

num_list = []
# Retrieve all of the span tags
span = soup('span')
#numbers = span.contents[0]
for span in span:
    numbers = span.contents[0]
    num_list.append(int(numbers))
    total = sum(num_list)
print (total)
