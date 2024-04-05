import regressive_count_module
print(' Welcome to the program ...')

while True:
    play_buttom = str(input('Press s to start or x to exit : '))
    if play_buttom == 's':
        try:
            number = int(input(' Write the value to count since it : '))
            time_speed = float(input(' Write the time speed here : '))
            regressive_count_module.Regressive_Count_Function(number, time_speed)
        except Exception as error :
            print(' The error is {}'.format(error))
    elif play_buttom == 'x':
        print(' Getting out ...')
        break
    else:
        print(' Press the button again ...')


print(' Finishing the program ...')