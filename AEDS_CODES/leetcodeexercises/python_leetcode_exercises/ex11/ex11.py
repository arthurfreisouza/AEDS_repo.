print( ' Welcome to this program.')

i = 0
sum = 0
count = 0
while i != 999:
    sum = sum + i
    count = count + 1
    i = float(input(' Write a number here to put in the list. \n'))

with open('/home/arthur/Desktop/my_new_file.txt', 'a') as arquivo:
    arquivo.write(' The sum is : {}. \n'.format(float(sum)))

print(' The size of this file is : {}'.format(count - 1))