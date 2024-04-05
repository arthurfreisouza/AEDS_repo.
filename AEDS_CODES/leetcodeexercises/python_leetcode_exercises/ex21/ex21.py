import function_module

print(' Welcome to this program.')
my_lst = []
while True:
    play_buttom = str(input('Press s to start or x to exit : '))
    if play_buttom == 's':   
        value = int(function_module.readint_function())
        my_lst.append(value)

    elif play_buttom == 'x':
        str = 'Getting out the game ...'
        print(len(str) * '=')
        print(str)
        print(len(str) * '=')
        break

    else:
        print(' Its not a right button, press another button, but now write it right.')


print(' The list of int number is : {}'.format(my_lst))