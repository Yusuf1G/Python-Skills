import re 

fname = input('Enter file name:')
fhand = open(fname)
numbers = []
for lines in fhand:
	lines = lines.rstrip()
	match = re.findall(r'[0-9]+',lines)
	#total = [int(match) for num in match]
	#print(total)

	for num in match:
		num_int = int(num)
		numbers.append(num_int)

total = sum(numbers)

print(numbers)
print(total)