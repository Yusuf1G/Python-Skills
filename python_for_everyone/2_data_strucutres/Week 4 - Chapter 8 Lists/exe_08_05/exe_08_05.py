fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

emails = []
count = 0

fh = open(fname)
for line in fh:
    line = line.strip()
    if not line.startswith('From '):
        continue
    sentence = line.split()
    email = sentence[1]
    emails.append(email)
    count += 1

for email in emails:
    print(email)
print("There were", count, "lines in the file with From as the first word")