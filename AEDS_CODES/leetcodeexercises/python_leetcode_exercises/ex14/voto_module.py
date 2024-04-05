def voto(name, year):
    """
        Explanation about the voto function :
        param 1 = Your name.
        param 2 = Year that you borned.
    """

    if ( 2024 - int(year) < 16):
        print(' Voto negado. \n')
        with open('/home/arthur/Desktop/my_new_file.txt', 'a') as my_file:
            my_file.write('{} = Voto negado. \n'.format(name))
    
    elif( (16 <= 2024 - int(year) < 18) or  (2024 - int(year) > 70) ):
        print(' Voto opcional. \n')
        with open('/home/arthur/Desktop/my_new_file.txt', 'a') as my_file:
            my_file.write('{} = Voto opcional. \n'.format(name))
    else:
        print(' Voto obrigatório. \n')
        with open('/home/arthur/Desktop/my_new_file.txt', 'a') as my_file:
            my_file.write('{} = Voto obrigatório. \n'.format(name))

    