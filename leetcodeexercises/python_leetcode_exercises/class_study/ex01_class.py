import class_person

print(' Welcome to the program ...')
lst = []
while True:
    try:
        start_or_exit = str(input(' Press s to start or x to exit.'))
    except Exception as error:
        print('This option is not right, error : {}. '.format(error))
    if start_or_exit == 's':
        print(' Now you will need to digit your data ...')
        try:
            your_name = str(input(' Write here your name : '))
            your_country = str(input(' Write here your country : '))
            your_date = str(input(' Write here your date of bird : '))
        except Exception as error:
            print(' Your data is not right, try again, but now digit it right !')  
        value = class_person.Person(your_name, your_country, your_date)
        my_age = value.getAge()
        my_name = value.getName()
        my_country = value.getCountry()
        my_date = value.getDateOfBirth()
        with open('/home/arthur/Desktop/ex_class.txt', 'a') as file:
            file.write('name = {}, country = {}, date of bird = {}, age = {}. \n'.format(my_name, my_country, my_date, my_age))
        lst.append(value)

    elif start_or_exit == 'x':
        print(' Getting out the program ...')
        break

    else:
        print(' Press the button again ...')


with open('/home/arthur/Desktop/ex_class.txt', 'r') as file:
    read_var = file.read()


print(20 * '=')
print('\n')
print(read_var)
print('\n')
print(20 * '=')