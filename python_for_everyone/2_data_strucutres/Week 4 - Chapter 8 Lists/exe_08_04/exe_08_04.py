fname = input('Enter file name: ')
fhand = open(fname)
lst = list()
for line in fhand:
	line = line.rstrip()
	sentence = line.split()
	for words in sentence:
		if words not in lst:
			lst.append(words)
	lst.sort()

#for words in lst:
print(lst)
