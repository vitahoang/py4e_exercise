import re

f_name = input("Enter file name: ")
if len(f_name) > 0: f_name = "regex_sum_382612.txt"
try:
    f_handle = open(f_name)
except:
    print('Something wrong with the file')
x_sum = 0        # Count of emails has been send by the most email sender

for line in f_handle:
    tml_re = re.findall('[0-9]+',line)
    for number in tml_re:
        x_sum = x_sum + int(number)

print(x_sum)