largest = None
smallest = None
num_list = []

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num_int = int(num)
        num_list.append(num_int)
    
    except:
        print('Invalid input')
            
    largest = max(num_list)
    smallest = min(num_list)        

print("Maximum", largest,'\nMinimum', smallest)