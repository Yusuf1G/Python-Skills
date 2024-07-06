fname = input('Enter file name: ')
fhand = open(fname)
count = 0
total = 0
for line in fhand: 
	if not line.startswith('X-DSPAM-Confidence:'):
		continue
	lines = float(line[19:])
	count = count + 1
	total = total + lines

print('Average spam confidence:', total / count)	
