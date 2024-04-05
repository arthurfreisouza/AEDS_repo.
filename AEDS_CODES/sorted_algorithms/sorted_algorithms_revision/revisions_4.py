import numpy as np


rand_val = np.random.randint(low = 0, high = 1000, size = 50) 
#print(rand_val)

def merge_sort(arr_ : list[int]) -> list[int]:
    if len(arr_) > 1: # Laço de parada.
        # Irei quebrar o array recursivamente em direita e esquerda.
        div_ = len(arr_) // 2
        left_ = arr_[ : div_].copy()
        right_ = arr_[div_ : ].copy()
        merge_sort(left_)
        merge_sort(right_)

        i = j = k = 0


        while (i < len(left_) and j < len(right_)): # Agora que já está tudo dividido, irei reordená-los os juntando.
            if (left_[i] < right_[j]):
                arr_[k] = left_[i]
                i += 1
            else:
                arr_[k] = right_[j]
                j += 1
            k += 1

        while i < len(left_):
            arr_[k] = left_[i]
            i += 1
            k += 1
        while j < len(right_):
            arr_[k] = right_[j]
            j += 1
            k += 1

    return arr_
    
print(merge_sort(rand_val.copy()))



def particao(arr_ : list[int], start, end) -> int:
    pivo = arr_[end] # O elemento pivo, nesse caso, será a última posição do array.

    aux = start - 1

    for i in range(start, end):
        if arr_[i] < pivo:
            aux += 1
            arr_[aux], arr_[i] = arr_[i], arr_[aux]
    arr_[aux + 1], arr_[end] = arr_[end], arr_[aux + 1] # Passando o elemento pivo para a sua posição correta na lista de valores.

    return aux + 1





def quick_sort(arr_ : list[int], start, end) -> list[int]:
    if start < end:
        pos = particao(arr_, start, end)
        quick_sort(arr_, start, pos - 1)
        quick_sort(arr_, pos + 1, end)

    return arr_


print(quick_sort(rand_val.copy(), 0, len(rand_val) - 1))