def primo(number_):
    count = 0
    for i in range(1, int(number_) + 1, 1):
        if int(number_) % i == 0:
            print('{} / {} = {}. \n'.format(int(number), i, int(number / i)))
            count = count + 1

    return count

while True:

    play_button = str(input(' Press c to continue or x to exit the game. \n'))

    if play_button == 'c':
        try:
            number = int(input(( 'Write a number to know if it is a cousin number. \n')))
        except Exception as error:
            print(' There is this error in the code : {}. \n'.format(error))
        else:
            return_value = int(primo(number))
            if return_value == 2:
                print(' {} is a cousin number. \n'.format(number))
            else:
                print(' {} is not a cousin number. \n'.format(number))

            print(' Number of multiples : {}'.format(int(return_value)))
    elif play_button == 'x':
        print(' Getting out the game ... \n')
        break
    else:
        print(' Invalid button. \n')



print(3 * '\n')
print(' Finishing the game .... \n')