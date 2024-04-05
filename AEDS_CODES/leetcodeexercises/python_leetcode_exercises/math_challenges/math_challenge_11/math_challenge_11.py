def Function_Code():
    sum = 0
    lst = []
    for i in range(10000000):
        lst.clear()
        counter = 0
        sum = sum + i
        for j in range(1, sum // 2 + 2):
            if (int(sum % j) == 0) and (j not in lst):
                lst.append(j)
                counter = counter + 1
                if counter == 500:
                    lst.append(sum)
                    return lst



my_lst = Function_Code()

print(my_lst[len(my_lst) - 1])
print(len(my_lst))
print(my_lst)