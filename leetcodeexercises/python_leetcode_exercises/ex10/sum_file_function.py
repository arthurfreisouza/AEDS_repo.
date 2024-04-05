import random

lst_of_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def sum_function(my_value):

    number = random.choice(lst_of_numbers)
    sum = number + my_value
    lst = [float(number), float(sum)]
    return lst