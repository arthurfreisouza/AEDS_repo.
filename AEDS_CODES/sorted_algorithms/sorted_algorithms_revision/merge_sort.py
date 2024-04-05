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