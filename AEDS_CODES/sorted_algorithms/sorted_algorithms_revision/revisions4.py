def bubble_sort(arr_ : list[int]) -> list[int]:
    for i in range(len(arr_) - 1, 0 -1):
        for j in range(len(arr_) - 1):
            if arr_[j] > arr_[j + 1]:
                arr_[j],arr_[j + 1] = arr_[j + 1], arr_[j]
    return arr_


print(f"Bubble sort : {bubble_sort([None])}")



def selection_sort(arr_ : list[int]) -> list[int]:
    for i in range(len(arr_)):
        min = i
        for j in range(i + 1, len(arr_) - 1):
            if arr_[min] > arr_[j]:
                min = j
        arr_[i],arr_[min] = arr_[min], arr_[i]
    return arr_


def insertion_sort(arr_ : list[int]) -> list[int]:
    for i in range(1, len(arr_)):
        elem = arr_[i]
        previous = i - 1
        
        while previous >= 0 and arr_[previous] > elem:
            arr_[previous + 1] = arr_[previous]
        
        arr_[previous + 1] = elem
    
    return arr_




def shell_sort(arr_ : list[int]) -> list[int]:
    intervalo = len(arr_) // 2

    while intervalo > 0:
        for i in range(intervalo, len(arr_)):
            elem = arr_[i]
            j = i
            while j >= intervalo and elem < arr_[j - intervalo]:
                arr_[j] = arr_[j - intervalo]
                j -= intervalo
            arr_[j] = elem
        intervalo = intervalo // 2
    

    return arr_


def merge_sort(arr_ : list[int]) -> list[int]:
    if len(arr_) > 1:
        div = len(arr_) // 2
        left = arr_[ : div].copy()
        right = arr_[div : ].copy()

        merge_sort(left)
        merge_sort(right)

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







def particao(arr_ : list[int], start, end):
    pivo = arr_[end]
    i = start - 1
    for j in range(start, end):
        if arr_[j] < pivo:
            i += 1
            arr_[i],arr_[j] = arr_[j], arr_[i]
    arr_[i + 1], arr_[end] = arr_[end], arr_[i + 1]
    return i + 1

def quick_sort(arr_, start, end) -> list[int]:
    if start < end:
        pos = particao(arr_, start, len(arr_))
        quick_sort(arr_,start, pos - 1)
        quick_sort(arr_, pos + 1, end)
    return arr_

