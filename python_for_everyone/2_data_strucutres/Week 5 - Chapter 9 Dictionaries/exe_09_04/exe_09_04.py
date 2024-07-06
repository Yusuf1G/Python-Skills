fname = input('Enter file name:')
if len(fname) < 1:
	fname = 'mbox-short.txt'

fhand = open(fname)

histogram = dict()

for lines in fhand: 
	if lines.startswith('From '):
		words = lines.split()
		email = words[1]
		histogram[email] = histogram.get(email,0)+1

		
emailname = None
emailcount = None

for email,count in histogram.items():
	if emailcount is None or count > emailcount:
		emailname = email 
		emailcount = count

#print a sorted dictionary based on count
#sorted_dict = list()
#for email,count in histogram.items():
#	sorted_dict.append((count,email))
#	sorted_dict = sorted(sorted_dict,reverse=True)
#print(sorted_dict)

print(sorted([(count,email) for email,count in histogram.items()],reverse=True))


#print (emailname,emailcount)