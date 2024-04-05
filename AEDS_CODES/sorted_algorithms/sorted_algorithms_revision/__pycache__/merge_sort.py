# Irei dividir o array recursivamente e irei montá-lo ordenando as posições.


def merge_sort(arr_ : list[int]) -> int:
    if len(arr_) > 1:
        div = len(arr_) // 2
        left = arr_[ : div].copy()
        right = arr_[div : ].copy()

        # Irei sempre ter os valores da direita e da esquerda de cada array para comparar
        merge_sort(left) 
        merge_sort(right)

        i, j, k = 0

        # Irei comparar as atuais pilhas para adicionar no meu array ordenado.
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
            arr_[k] = left[j]
            j += 1
            k += 1

    return arr_
    
