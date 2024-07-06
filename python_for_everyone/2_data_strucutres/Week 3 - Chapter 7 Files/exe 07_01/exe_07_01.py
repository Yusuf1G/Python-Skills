# Use words.txt as the file name
fname = input("Enter file name: ")
try:
    fhand = open('C:\\Users\\yusuf\\Documents\\Coursera\\Python\\Data Strucutres\\exe 07_01\\'+ fname)

    for line in fhand:
        data = line.rstrip()
        lines = data.upper()
        print(lines) 

except:
    print("File cannot be opened:", fname)