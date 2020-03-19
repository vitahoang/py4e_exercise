try:
    rate = float(input('Enter rate:'))
except:
    print('Please enter a numeric')
    quit()
try:
    hours = float(input('Enter working hours:'))
except:
    print('Please enter a numeric')
    quit()
extra_hours = hours - 40
if extra_hours <= 0:
    salary = rate * hours
else:
    salary = rate * 40 + rate * 1.5 * extra_hours
print('Pay:', salary)
