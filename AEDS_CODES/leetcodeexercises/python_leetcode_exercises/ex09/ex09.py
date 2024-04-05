print(' Welcome to this program. Here we will create a calculator.')

while True:
    value = float(input(' Write a value to see its multiplication table : '))
    if value < 0:
        print(' Its a negative number. \n')
        break
    for i in range(11):
        print('{} x {} = {} \n'.format(float(value), float(i), float(value * i)))