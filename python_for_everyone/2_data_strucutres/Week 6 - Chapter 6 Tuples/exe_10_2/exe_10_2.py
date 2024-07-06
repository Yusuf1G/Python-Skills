fname = input('Enter file name:')
if len(fname) < 1:
	fname = 'mbox-short.txt'

fhand = open(fname)

tracker = dict()

for lines in fhand: 
	if lines.startswith('From '):
		words = lines.split()
		time = words[5]
		hour = time[:2]

		tracker[hour] = tracker.get(hour,0)+1

sortedtracker = sorted(tracker.items())

for k,v in sortedtracker:
	print(k,v)
	
#for items in sortedtracker:
#	print(items[0],items[1])
