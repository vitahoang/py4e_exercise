try:
    scr = float(input('Please input your score:'))
except:
    print('Please input a numeric!')
    quit()

if scr > 1:
    print('Your score is out of range')
    quit()
elif scr < 0:
    print('Your score is out of range')
    quit()
elif scr >= 0.9:
    print('A')
elif scr >= 0.8:
    print('B')
elif scr >= 0.7:
    print('C')
elif scr >= 0.6:
    print('D')
else:
    print('E')