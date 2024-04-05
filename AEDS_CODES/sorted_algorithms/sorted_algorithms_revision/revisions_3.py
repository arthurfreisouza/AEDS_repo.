def shell_sort(arr_ : list[int]) -> list[int]:
    intervalo = len(arr_) // 2
    while intervalo > 0: # Irei realizar o loop enquanto eu puder dividir o array.
        for i in range(intervalo, len(arr_)):
            elem = arr_[i]
            j = i
            while j >= intervalo and arr_[j - intervalo] > elem: # O elemento da posição mais a esquerda é maior do que o elemento da posição mais a direita.
                arr_[j] = arr_[j - intervalo]
                j -= intervalo
            arr_[j] = elem

        intervalo //= 2 
    return arr_

print(f"Shell sort : {shell_sort([10, 20, 7, 17, 4, 2])}")


def merge_sort(arr_ : list[int]) -> list[int]:
    if len(arr_) > 1:
        div = len(arr_) // 2
        left = arr_[ : div].copy()
        right = arr_[div : ].copy()

        merge_sort(left)
        merge_sort(right)


        i = j = k = 0

        while (i < len(left) and j < len(right)):
            if left[i] > right[j]:
                arr_[k] = right[j]
                j += 1
            else:
                arr_[k] = left[i]
                i += 1
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


print(f"Merge sort : {merge_sort([100, 99, 1, 110, 2, 3, 4, 5, 10, 20])}")


def particao(arr_ : list[int], start, end):
    pivo_element = arr_[end]
    aux = start - 1
    for i in range(start, end):
        if arr_[i] <= pivo_element:
            aux += 1
            arr_[aux],arr_[i] = arr_[i], arr_[aux]
    arr_[aux + 1], arr_[end] = arr_[end], arr_[aux + 1]
    return aux + 1 # Tenho que retornar a posição do pivo.
        


def quick_sort(arr_ : list[int], start, end) -> list[int]:
    if start < end:
        pos = particao(arr_, start, end)
        quick_sort(arr_, start, pos - 1)
        quick_sort(arr_, pos + 1, end) 

    return arr_


print(f"Quick sort : {quick_sort([100, 99, 1, 110, 2, 3, 4, 5, 10, 20], 0, 9)}")