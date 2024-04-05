def eletronic_box_function(value):
    count_50 = 0
    count_20 = 0
    count_10 = 0
    count_5 = 0
    count_1 = 0

    while True:
        while float(value) - 50 > 0:
            print(float(value))
            value = float(value) - 50
            count_50 = count_50 + 1

        while float(value) - 20 > 0:
            print(float(value))
            value = float(value) - 20
            count_20 = count_20 + 1

        while float(value) - 10 > 0:
            print(float(value))
            value = float(value) - 10
            count_10 = count_10 + 1
            
        while float(value) - 5 > 0:
            print(float(value))
            value = float(value) - 5
            count_5 = count_5 + 1

        while float(value) - 1 >= 0:
            print(float(value))
            value = float(value) - 1
            count_1 = count_1 + 1

        print(float(value))
        if float(value) < 1:
            break


    lst = [count_50, count_20, count_10, count_5, count_1, float(value)]
    return lst

