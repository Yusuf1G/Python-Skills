import urllib.request, urllib.parse, urllib.error 
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter Location: ')
print('Retrieving', url,)

connection = urllib.request.urlopen(url, context=ctx)
data = connection.read().decode()

info = json.loads(data)
print('Retrieved ',len(data),' characters')

list_of_dicts = info['comments']
print('Count:',len(list_of_dicts))

counts = []

for item in list_of_dicts:
    count = int(item['count'])
    counts.append(count)
    total = sum(counts)    

print('Sum:',total)