import sum_function

print(' Welcome to this program. \n')
while True:
    continue_code = str(input(' Press s to continue or x to exit the game. \n'))
    if continue_code == 's':
        try:
            multiple = int(input('Write a multiple value here : \n'))
            final_value = int(input('Write a final value here : \n'))

        except Exception as error:
            print(' Error = {}'.format(error))
        else:
            my_result = sum_function.sum_func(final_value, multiple)
            print(' The sum of multiples of the number {} until {} is : {}'.format(int(multiple), int(final_value), int(my_result)))
    elif continue_code == 'x':
        print(' Getting out the game ... \n')
        break
    else:
        print(' Its not a right button. Press another button to play the game. \n')


print('*' * 50)
print(' ' * 20, 'Finishing the game ! \n')
print('*' * 50)