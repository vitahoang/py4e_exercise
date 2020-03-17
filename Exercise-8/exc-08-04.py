fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('Something wrong with the file')
lst = list()
for line in fh:
    wil = line.split()
    for i in wil:
        if i in lst: continue
        lst.append(i)
lst.sort()
print(lst)
