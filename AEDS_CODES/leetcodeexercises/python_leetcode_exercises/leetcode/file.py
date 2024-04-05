import sys


lst_ = []
while True:
    try:
        number = int(input(' 1 to first light bulb, 2 to second light bulb'))
        if (number == 1) or (number == 2):
            lst_.append(int(number))
        else:
            print(' This value is not right.')
            continue
    except Exception:
        print('Errors is happening')
        break

print(lst_)
lst_len_ = len(lst_)
print(lst_len_)

if (lst_len_ <= 2 or lst_len_ >= 100000):
    sys.exit()

light_1 = False
light_2 = False

for decision in lst_:
    if decision == 1:
        if light_1 == True:
            light_1 == False
        else:
            light_1 = True
    elif decision == 2:
        if light_1 == True and light_2 == True:
            light_1 = False
            light_2 = False
        elif light_1 == True and light_2 == False:
            light_1 = False
            light_2 = True
        elif light_1 == False and light_2 == True:
            light_1 = True
            light_2 = False
        else:
            light_1 = True
            light_2 = True

if light_1 == True:
    print('1')
else:
    print('0')
if light_2 == True:
    print('1')
else:
    print('0')