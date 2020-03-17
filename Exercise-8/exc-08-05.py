fname = input("Enter file name: ")
if len(fname) > 0: fname = "mbox-short.txt"
try:
    fh = open(fname)
except:
    print('Something wrong with the file')
count = 0
ls = list()
for line in fh:
    if not line.startswith("From ") : continue
    count = count + 1
    lsp = line.split()
    email = lsp[1].strip("(){}<>;")
    ls.append(email)
    print(email)

print("There were", count, "lines in the file with From as the first word")