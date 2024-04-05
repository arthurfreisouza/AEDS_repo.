import function_module
print('Welcome to this program. \n')
lst_of_numbers = []
while True:
    play_button = str(input('Press s to insert or x to exit : \n'))
    if play_button == 's':
        try:
            value = float(input('S pressed, write a value to put in the list. \n'))
        except Exception as error:
            print(' This is the error : {}. \n'.format(error))
        else:
            lst_of_numbers.append(value)
    elif play_button == 'x':
        print(' Getting out the program ... \n')
        break
    else:
        print(' Wrong button, press it again ... \n')

media = function_module.media_function(lst_of_numbers)
bigger = function_module.bigger_function(lst_of_numbers)
lower = function_module.lower_function(lst_of_numbers)

print(' The media of this list {} is : {}. \n'.format(lst_of_numbers, media))
print(' The biggets number is : {}. \n'.format(bigger))
print(' The lowest number is : {}. \n'.format(lower))