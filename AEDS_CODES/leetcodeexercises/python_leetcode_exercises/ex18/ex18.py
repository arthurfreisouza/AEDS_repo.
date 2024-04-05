import table_module

print(' Welcome to the program. \n')
while True:
    play_button = str(input(' Press s to start or x to exit. \n'))
    if play_button == 's':
        try:
            num_1 = int(input('Write here the first number : '))
            num_2 = int(input('Write here the second number : '))
        except ValueError as error:
            print('You putted a wrong value')
        except Exception as error:
            print(' Error : {}'.format(error))
        else:
            print('''
                    [1] Somar
                    [2] Multiplicar
                    [3] Maior
                    [4] Novos Números
                    [5] Sair Do Programa
                  ''')
            my_choice = int(input(' Select a number of the list above ... \n'))
            if my_choice == 1:
                sum_var = table_module.sum(num_1, num_2)
                print(' The sum is : {}. \n'.format(sum_var))
            elif my_choice == 2:
                multp_var = table_module.multiply(num_1, num_2)
                print(' The multiply is : {}. \n'.format(multp_var))
            elif my_choice == 3:
                if num_1 >= num_2:
                    print(' The bigger number is : {}. \n'.format(num_1))
                else:
                    print(' The bigger number is : {}. \n'.format(num_2))
            elif my_choice == 4:
                num_1 = int(input('Write here the first number : \n'))
                num_2 = int(input('Write here the second number : \n'))
                print(' New numbers :{}, {}. \n'.format(num_1, num_2))
            elif my_choice == 5:
                print(' Getting out the code ... \n')
                break
            else:
                print('Its number is not right. \n')
    elif play_button == 'x':
        print(' Getting out the game ... \n')
        break
    else:
        print(' Press again, this button is not right. \n')
print(2 * '\n')
print(' Finishing the program. \n')
print(2 * '\n')