import ficha_module

print(' Welcome to the program. ')

while True:
    button = str(input(' Press s to start or x to exit : '))
    if button == 's':
        name = input(' Write your name here : ')
        points = input(' How many points did you have ? ')

        
        if str(name) == '' and str(points) == '':
            ficha_module.ficha_function()
        elif str(name) != '' and str(points) == '':
            ficha_module.ficha_function(name)
        elif str(name) == '' and str(points) != '':
            ficha_module.ficha_function(' < desconhecido > ',points)
        else:
            ficha_module.ficha_function(name, points)

    elif button == 'x':
        print(' Getting out the game ...')
        break
    else:
        print(' Press the right button ...')

print(' Finishing the program ...')

with open('/home/arthur/Desktop/ex24.txt', 'r') as file:
    var = file.read()

print(var)