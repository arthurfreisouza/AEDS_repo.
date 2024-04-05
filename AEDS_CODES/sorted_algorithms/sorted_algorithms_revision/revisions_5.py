def merge_sort(arr_ : list[int]) -> list[int]:
    if len(arr_) > 1:
        # Separar o array em esquerad e direita.
        div = len(arr_) // 2
        left_ = arr_[ : div].copy()
        right_ = arr_[div : ].copy()
        
        # Chamar a função recursiva.
        merge_sort(left_)
        merge_sort(right_)

        # Variáveis de controle.
        i = j = k = 0

        # Loop para a construção do array.
        while (i < len(left_) and j < len(right_)):
            if left_[i] < right_[j]:
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

print(merge_sort([10, 20, 5, 2, 40]))


def particao(arr_ : list[int], start_, end_):
    # O elemento pivo que será comparado é o último elemento do array.
    pivo = arr_[end_]
    aux = start_ - 1
    # Loop para comparar todos os valores com o elemento pivo.
    for i in range(start_, end_):
        if arr_[i] < pivo:
            aux += 1
            # Caso eu ache um elemento menor que o elemento pivo, irei colocá-lo no começo da lista com o auxílio de 1 variável auxiliar que conterá os index's.
            arr_[aux], arr_[i] = arr_[i], arr_[aux]
    
    # Trocando o elemento pivo de posição, e o colocando na sua posição correta.
    arr_[aux + 1], arr_[end_] = arr_[end_], arr_[aux + 1]

    return aux + 1 # Retornando o índice do elemento pivo, para eu usar recursão em ambas as partes.




def quick_sort(arr_ : list[int], start, end) -> list[int]:
    if (start < end):
        pos = particao(arr_, start, end )

        quick_sort(arr_, start, pos - 1)
        quick_sort(arr_, pos + 1, end)
    return arr_

print(quick_sort([10, 20, 5, 2, 40],0 ,4))







def shell_sort(arr_ : list[int]) -> list[int]:
    # Pegando a metade do array para usar de intervalo.
    middle = len(arr_ ) // 2

    while middle > 0:
        for i in range(middle, len(arr_)):
            # Pegando o valor a ser comparado toda vez
            elem  = arr_[i]
            j = i
            while j > middle and arr_[j - middle] > elem:
                arr_[j] = arr_[j - middle]
                j -= middle
            arr_[j] = elem
        middle = middle // 2

    return arr_


def insertion_sort(arr_ : list[int]) -> list[int]:
    for i in range(1, len(arr_)): # Varrerei todas as posições antes desse tempo marcado.
        high_elem = arr_[i] # Pegando o elemento que será comparado.
        k = i - 1
        while k > 0 and arr_[k] > high_elem:
            arr_[k + 1] = arr_[k]
            k -= 1
        arr_[k + 1] = high_elem

    return arr_



def bubble_sort(arr_ : list[int]) -> list[int]:
    for i in range(0, len(arr_)):
        for j in range(len(arr_) - i - 1):
            if arr_[j] > arr_[j + 1]:
                temp = arr_[j]
                arr_[j] = arr_[j + 1]
                arr_[j + 1] = temp
    return arr_

print(bubble_sort([10, 2, 13, 7, 4]))

def selection_sort(arr_ : list[int]) -> list[int]:
    for i in range(len(arr_)):
        min = i
        for j in range(i + 1, len(arr_)):
            if arr_[j] < arr_[min]:
                min = j # Irei ter o índice que contém o menor valor.
        arr_[i], arr_[min] = arr_[min], arr_[i]

    return arr_

print(selection_sort([10, 2, 13, 7, 4]))