import sum_file_function

print(' Welcome to the game. \n')
my_points = 0
machine_points = 0
button_start = str(input(' Press s to start the game or x for stop. \n'))
while True:

    if button_start == 'x':
        print(' Getting out the game ...')
        break

    choice = str(input(' Will you choice pair or unpair ? \n'))
    number = int(input(' Wich number will you choice in this game? \n'))
    game_result = []
    game_result = sum_file_function.sum_function(number)
    game_sum = float(game_result[1])

    if (game_sum % 2 == 0 and choice == 'pair'):
        print(' Machine number : {} \n'.format(game_result[0]))
        print(' You won the game !!! \n')
        my_points = my_points + 1  
    elif (game_sum % 2 != 0 and choice == 'unpair'):
        print(' Machine number : {} \n'.format(game_result[0]))
        print(' You won the game !!! \n')
        my_points = my_points + 1
    else:
        print(' Machine number : {} \n'.format(game_result[0]))
        print(' You lose the game !!! \n')
        machine_points = machine_points + 1

    button_start = str(input(' Press s to continue the game or x for stop. \n'))

print(' Machine : {}, you {}. \n'.format(machine_points, my_points))