

def selection_sort(arr_ : list[int]) -> list[int]:
    for i in range(len(arr_)):
        min = i
        for j in range(i + 1, len(arr_)):
            if arr_[min] > arr_[j]:
                min = j
        temp = arr_[i]
        arr_[i] = arr_[min]
        arr_[min] = temp

    return arr_
import numpy as np


def merge_sort(arr_ : list[int]):

    # Dividindo todo o array para arrays únicos.
    if len(arr_) > 1:
        division = len(arr_) // 2
        right = arr_[division:].copy()
        left = arr_[:division].copy()
    merge_sort(right)
    merge_sort(left)

    # Agora, o array está todo dividido, e poderá começar a ser montado com 

    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr_[k] = left[i]
            i += 1
        else:
            arr_[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr_[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
       arr_[k] = right[j]
       j += 1
       k += 1
    return arr_


def bubble_sort(arr_ : list[int]) -> list[int]:
    for i in range(len(arr_)):
        for j in range(0, len(arr_) - 1 - i):
            if arr_[j + 1] < arr_[j]: 
                temp = arr_[j]
                arr_[j] = arr_[j + 1]
                arr_[j + 1] = temp
    
    return arr_


def bubble_sort_rec(arr_ : list[int], size : int):

    if size == 1:
        return arr_
    
    else:
        for i in range(size):
            if arr_[i] > arr_[i + 1]:
                temp = arr_[i]
                arr_[i] = arr_[i + 1]
                arr_[i + 1] = temp

    return (arr_, size - 1)








def insertion_sort(arr_ : list[int]) -> list[int]:
    for i in range(1, len(arr_)):
        element = arr_[i]
        previous = i - 1

        while previous >= 0 and element < arr_[previous]:
            arr_[previous + 1] = arr_[previous]
            previous -= 1
        arr_[previous + 1] = element




    def shell_sort(arr_ : list[int]) -> list[int]:
        intervalo = len(arr_) // 2

        while intervalo > 1:

            for i in range(intervalo, len(arr_)):
                temp = arr_[i]
                j = i

                while j >= intervalo and arr_[j - intervalo] > temp:
                    arr_[j] = arr_[j - intervalo]
                    j -= intervalo
                arr_[j] = temp            



            intervalo = intervalo // 2
        return arr_