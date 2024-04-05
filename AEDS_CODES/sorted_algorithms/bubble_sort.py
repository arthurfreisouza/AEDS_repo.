import numpy as np

# O custo computacional é alto.
def bubble_sort(my_lst):
    size = len(my_lst)
    for i in range(size): 
        for j in range(0, size - 1 -i): # Para cada iteração de j, irei levar o maior elemento para o mais a direita possivel. Quando eu sair do loop j, o maior elemento estará na direita.
            if my_lst[j] >= my_lst[j + 1]: 
                aux = my_lst[j]
                my_lst[j] = my_lst[j + 1]
                my_lst[j + 1] = aux

    return my_lst

print(bubble_sort([15, 32, 8, 3]))



def bubble_sort_rec(arr_, len_): # Resolução através de recursão.
    if len_ == 1:
        return arr_
    
    for i in range(len_ - 1):
        if arr_[i] >=  arr_[i + 1]:
            temp = arr_[i]
            arr_[i] = arr_[i + 1]
            arr_[i + 1] = temp
    
    return bubble_sort_rec(arr_, len_ - 1)



values = str(input()).split(" ")
values = list(map(int, values))

print(bubble_sort_rec(values, len(values)))