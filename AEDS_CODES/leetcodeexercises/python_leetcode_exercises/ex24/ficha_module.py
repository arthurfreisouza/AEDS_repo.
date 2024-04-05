def ficha_function(name_ = '< desconhecido > ', points_ = 0):
    with open('/home/arthur/Desktop/ex24.txt', 'a') as file:
        file.write(' Name = {}, points = {} \n'.format(name_, points_))