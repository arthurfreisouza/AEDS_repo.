import Curso_python.ex.ex01.calcula_media as calcula_media
my_list = []

while True:
    try:
        value = int(input(' Write a number to put in the list !'))
        my_list.append(value)
    except ValueError:
        print(" You wished stop to put values in the list !")
        break

print("The list is : {}".format(my_list))

my_media = calcula_media.media(my_list)

print(' The media of these values is : {}'.format(my_media))