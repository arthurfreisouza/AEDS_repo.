def my_function() -> tuple:
    n1 = 0
    n2 = 0
    n3 = 0
    greater_product = 0

    for i in range(100):
        for j in range(100):
            for k in range(100):
                product = i * j * k
                str_product = str(product)
                length_number = len(str_product)

                if length_number % 2 == 0:
                    aux = 1
                    for a in range(length_number):
                        if str_product[a] != str_product[length_number - 1 - a]:
                            aux = 0
                            break

                    if aux == 1 and greater_product < int(product):
                        greater_product = int(product)
                        n1 = i
                        n2 = j
                        n3 = k

    return (n1, n2, n3, greater_product)


def my_function2() -> tuple:
    n1 = 0
    n2 = 0
    greater_product = 0

    for i in range(100):
        for j in range(100):
            product = i * j
            str_product = str(product)
            length_number = len(str_product)
            if length_number % 2 == 0:
                aux = 1
                for a in range(length_number):
                    if str_product[a] != str_product[length_number - 1 - a]:
                        aux = 0
                        break
                if aux == 1 and greater_product < int(product):
                    greater_product = int(product)
                    n1 = i
                    n2 = j

    return (n1, n2, greater_product)













print('Welcome to the program.')

my_tuple = my_function()

print('The palindrome number is: {}, which is the product of {} x {} x {}.'.format(my_tuple[3], my_tuple[0], my_tuple[1], my_tuple[2]))

my_tuple_2 = my_function2()
print('The palindrome number is: {}, which is the product of {} x {}.'.format(my_tuple_2[2], my_tuple_2[0], my_tuple_2[1]))




