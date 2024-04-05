import numpy as np
import random

random_numbers = []

for i in range(100):
    random_numbers.append(random.randint(0, 1000))
#print(random_numbers)
def bubble_sort(arr_ : list[int]) -> list[int]:
    # Complexidade O(n²)
    # Pegar oa array, e levar o maior elemento, a cada iteração, para a posição mais direita da fila.
    # A cada rodada o algoritmo irá ficando mais ordenado.
    size_arr = len(arr_)

    for i in range(size_arr):
        for j in range(0, size_arr - 1 - i): # A cada aumento de i implica que o final do array está ordenado.
            if arr_[j] > arr_[j + 1]: # Se o valor mais a esquerda é maior, então jogue ele para mais a direita na lista.
                temp = arr_[j]
                arr_[j] = arr_[j + 1]
                arr_[j + 1] = temp

    return arr_


#print(bubble_sort(random_numbers))





random_numbers = []

for i in range(100):
    random_numbers.append(random.randint(0, 1000))

print(random_numbers)

#arr_ = str(input(" Write the array ... ")).split(" ")
#size_arr = len(arr_)


def bubble_sort_rec(arr_ : list[int], size : int) -> list[int]:

    if size == 1:
        return arr_
    for i in range(size - 1):
        if arr_[i] > arr_[i + 1]:
            temp = arr_[i]
            arr_[i] = arr_[i + 1]
            arr_[i + 1] = temp
    
    return bubble_sort_rec(arr_, size - 1)
    


#bubble_sort_rec(arr_, size_arr)
print(bubble_sort_rec(random_numbers, len(random_numbers)))
