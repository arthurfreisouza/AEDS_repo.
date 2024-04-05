import random_elements
import sum_of_values

my_list = []

while True:
    try:
        value = input('Write a number and put it in this list (or type "x" to exit): ')
        if value.lower() == 'x':
            break
        value = int(value)
        my_list.append(value)
    except ValueError:
        print('Write an integer number.')



    

numbers_selected = random_elements.random_list_elements(my_list)

total_sum = sum_of_values.sum(numbers_selected)

print(' The numbers selected are : {}. \n'.format(numbers_selected))
print(' The sum of the pair values is : {}.\n'.format(total_sum))