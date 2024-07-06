import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter XML URL:')
info = urllib.request.urlopen(url, context=ctx)

data = info.read().decode()
print('Retrieved', len(data), 'characters')

num=[]
tree = ET.fromstring(data)
nameslist = tree.findall('comments/comment')
for name in nameslist:
	counters = name.find('count').text
	numbers = int(counters)
	num.append(numbers)
	total = sum(num)
print('Count:', len(num))
print('Sum:', total)

