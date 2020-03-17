fname = input("Enter file name: ")
try:
    fhand = open(fname)
except:
    print('Something wrong with the file')
for line in fhand:
    print((line.upper()).rstrip())