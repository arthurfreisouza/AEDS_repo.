import my_module
import time

start_time = time.time()
with open('/home/arthur/Desktop/aux.txt', 'r') as file:
    number_within_file = file.read()

number_within_file = int(number_within_file)

lst_of_returned_values = []


lst_of_returned_values = my_module.Number_Function(number_within_file)

product = 1
for i in lst_of_returned_values:
    product = product * i


print(' Prime numbers : {}.'.format(lst_of_returned_values))
print(' The prime product of the number {} is {}'.format(number_within_file, product))
end_time = time.time()

time_wasted = end_time - start_time
print(' The time wasted in this program is {}. '.format(time_wasted))