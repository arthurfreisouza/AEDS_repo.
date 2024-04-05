import bigger

lst = []

while True:
    value = str(input(' Write a number to add in the list : '))
    if value == 'x':
        break
    lst.append(float(value))

bigger_number = bigger.bigger_function(lst)
print('\n')
print(' The biggest number in the list is : {}'.format(bigger_number))