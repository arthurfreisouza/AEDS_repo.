import voto_module

print(' Welcome to this program ! \n')

print(voto_module.voto.__doc__)
with open('/home/arthur/Desktop/my_new_file.txt', 'w') as my_file:
    my_file.truncate()

while True:
    insert = str(input(' Press i to insert or x to exit the game ! \n'))
    if insert == 'x':
        print(' Getting out the game ... \n')
        break
    my_name = str(input(' Write here your name : \n'))
    my_year = int(input(' Write here the year you borned : \n'))
    voto_module.voto(my_name, my_year)




for i in range(4):
    print(30 * '=' )

print(' Finishing ... \n')
with open('/home/arthur/Desktop/my_new_file.txt', 'w') as my_file:
    my_file.truncate()

for i in range(4):
    print(30 * '=' )
    print()