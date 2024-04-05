def bigger_function(lst):
    maior = 0
    for i in range(len(lst)):
        if lst[maior] < lst[i]:
            maior = i

    return lst[maior]