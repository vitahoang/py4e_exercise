num = 0
tot = 0.0
while True:
    rval = input('Enter a random number:')
    if rval == 'done':
        print('Here is your result')
        break
    try:
        ival = int(rval)
    except:
        print("Bad data")
        continue
    num = num + 1
    tot = tot + ival
print(tot,num,tot/num)
print('All Done')