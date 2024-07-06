largest = None
smallest = None
numlist = []

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num_int = int(num)
        numlist.append(num_int)
    except:
        print('Invalid input')

if numlist:
    largest = max(numlist)
    smallest = min(numlist)
    print("Maximum", largest, "Minimum", smallest)

else: 
    print('No numbers found in the list')