import factorial

print(' Welcome to this program. \n')

while True:
    play_button = str(input(' Press c to continue or x to exit the game. \n'))
    if play_button == 'c':
        number = int(input('Write a number to calcule the factorial. \n'))
        show = str(input('Write True or False to show or dont show the multiplication. \n'))
        if str(show).lower() == 'true':
            show = bool(True)
        elif str(show).lower() == 'false':
            show = bool(False)
        else:
            print(' Its not a valid value, digit it again. \n')

        factorial.factorial_function(number, show)

    elif play_button == 'x':
        print(' Getting out the game... \n')
        break

    else:
        print(' Its not a right button, try another way. \n')

print(3 * '\n')
print(' Finishing the game... \n')