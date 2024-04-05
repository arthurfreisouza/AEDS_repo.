import eletronic_box

my_value = float(input(' Write the value that you have on your wallet now here : '))

my_money = []

my_money = eletronic_box.eletronic_box_function(my_value)

print(' You will have {} notes of 50 dollars.'.format(my_money[0]))
print(' You will have {} notes of 20 dollars.'.format(my_money[1]))
print(' You will have {} notes of 10 dollars.'.format(my_money[2]))
print(' You will have {} notes of 5 dollars.'.format(my_money[3]))
print(' You will have {} notes of 1 dollar.'.format(my_money[4]))
print(' You will have {} dollars of rest.'.format(my_money[5]))
