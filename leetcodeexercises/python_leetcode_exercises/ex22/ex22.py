import functions_module

print('Welcome to the program.')
lst_of_names = []
lst_of_ages = []
lst_of_geners = []
with open('/home/arthur/Desktop/my_new_file_1.txt', 'w') as file:
    pass
with open('/home/arthur/Desktop/my_new_file_2.txt', 'w') as file:
    pass
with open('/home/arthur/Desktop/my_new_file_3.txt', 'w') as file:
    pass


while True:
    play_button = str(input(' Press s to start or x to exit : '))
    if play_button == 's':
        try:
            value_name = str(input(' Write a name here : '))
            lst_of_names.append(value_name)

            value_age = int(input(' Write a age here : '))
            lst_of_ages.append(value_age)

            value_gener = str(input(' Write a gener here : '))
            lst_of_geners.append(value_gener)
            
        except Exception as error:
            print(' The error is : {}'.format(error))

    elif play_button == 'x':
        print(' Getting out the game ... ')
        break
    else:
        print('Press again ... ')


for i in range(len(lst_of_ages)):
    with open('/home/arthur/Desktop/my_new_file_1.txt', 'a') as file:
        file.write(str(lst_of_names[i]))
        file.write(' ')
        file.write(str(lst_of_ages[i]))
        file.write(' ')
        file.write(str(lst_of_geners[i]))
        file.write('\n')




media_returned = functions_module.Media_Function(lst_of_ages)
print(' Reading the complete file ...')
with open('/home/arthur/Desktop/my_new_file_1.txt', 'r') as file:
    show = file.read()

print(len(lst_of_ages) * '=')
print('\n')
print(show)
print('\n')
print(len(lst_of_ages) * '=')



print(' Now, i will read the file that have only mens...')
functions_module.Descrescent_Age_Men(lst_of_names, lst_of_ages, lst_of_geners) # As listas serão parâmetros das funções.
with open('/home/arthur/Desktop/my_new_file_2.txt', 'r') as file:
    show2 = file.read()

print(len(lst_of_ages) * '=')
print('\n')
print(show2)
print('\n')
print(len(lst_of_ages) * '=')

print(' Now, i will read the file that have only womens that are newer than 20...')
girls_newer_than_20 = functions_module.Girls_Older_Than_20(lst_of_names, lst_of_ages, lst_of_geners) # As listas serão parâmetros das funções.
with open('/home/arthur/Desktop/my_new_file_3.txt', 'r') as file:
    show3 = file.read()

print(len(lst_of_ages) * '=')
print('\n')
print(show3)
print('\n')
print(len(lst_of_ages) * '=')


print(' There are {} girls that are newer than 20 years. '.format(int(girls_newer_than_20)))
print(' The media is : {}'.format(media_returned))
