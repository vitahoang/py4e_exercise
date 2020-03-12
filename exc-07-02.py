fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('Something wrong with the file')
total = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    ffloat = int(line.find('.'))
    total = total + float(line[(ffloat - 1):])
    count = count + 1
print("Average spam confidence:", total/count)