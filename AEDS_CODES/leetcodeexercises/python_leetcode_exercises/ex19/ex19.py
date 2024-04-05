import fibonacci_module

print(' Welcome to the program. \n')

while True:
    play_button = str(input('Press s to start or x to exit : \n'))
    if play_button == 's':
        try:
            number = int(input(' Write the number here : \n'))
        except Exception as error:
            print(' This is the error : {}. \n'.format(error))
        else:
            lst_return = []
            lst_return = fibonacci_module.fibonacci(number)
            print(' The list is until the {} term is {}. \n'.format(number, lst_return))
    elif play_button == 'x':
        print(' Getting out the program ... \n')
        break
    else:
        print(' Wrong button, press it again ... \n')

print(2 * '\n')
print(' Finishing ... \n')
print(2 * '\n')