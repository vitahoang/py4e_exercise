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
salary = 0
def computepay(r,h,eh):
    if eh <= 0:
        salary = r * h
    else:
        salary = r * 40 + r * 1.5 * eh
    print('Pay', salary)
    return salary

computepay(rate,hours,extra_hours)
