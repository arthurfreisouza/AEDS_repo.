def fibonacci(number_):
    lst = [int(0), int(1)]
    count = 0
    for i in range(2,int(number_)):
        lst.append(lst[i - 1] + lst[i - 2])

    return lst