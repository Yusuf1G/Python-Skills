largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
        try:
            num_int = int(num)
        except:
            print('Invalid input')
            
        largest = max(int_num)
        smallest = min(int_num)        
                
    print(num)

print("Maximum", largest)