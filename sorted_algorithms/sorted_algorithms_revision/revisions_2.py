import numpy as np



def bubble_sort1(arr_ : list[int]) -> list[int]:
    for i in range(len(arr_) - 1, 0, -1):
        for j in range(len(arr_) - 1):
            if arr_[j] > arr_[j + 1]:
                temp = arr_[j]
                arr_[j] = arr_[j + 1]
                arr_[j + 1] = temp

    return arr_


def bubble_sort2(arr_ : list[int]) -> list[int]:
    for i in range(len(arr_)):
        for j in range(len(arr_) - i - 1):
            if arr_[j] > arr_[j + 1]:
                temp = arr_[j]
                arr_[j] = arr_[j + 1]
                arr_[j + 1] = temp
    return arr_


print(f"BUBBLE SORT1 : {bubble_sort1([10, 95, 33, 1, 3, 4])}")
print(f"BUBBLE SORT2 : {bubble_sort2([10, 95, 33, 1, 3, 4])}")


########################## buble sort ok.




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

print(f"SELECTION SORT : {selection_sort([10, 95, 33, 1, 3, 4])}")



######################### selection sort ok.


def insertion_sort(arr_ : list[int]) -> list[int]:
    for i in range(1, len(arr_)):
        element = arr_[i]
        previous = i - 1

        while previous >= 0 and element < arr_[previous]:
            arr_[previous + 1] = arr_[previous]
            previous -= 1
        arr_[previous + 1] = element
    return arr_

print(f"INSERTION SORT : {insertion_sort([10, 95, 33, 1, 3, 4])}")




##################### Insertion sort ok.





def shell_sort(arr_ : list[int]) -> list[int]:
    intervalo = len(arr_) // 2
    while intervalo > 0: # Irei executar enquanto puder dividir o valor do intervalo pela metade.
        for i in range(intervalo, len(arr_)):
            temp = arr_[i] # Pegarei os valores da 2 parte do intervalo.
            j = i
            while j >= intervalo and arr_[j - intervalo] > temp: # Comparando a primeira parte do intervalo com a 2 parte do intervalo.
                arr_[j] = arr_[j - intervalo] # Passando a maior posição para a parte final
                j -= intervalo
            arr_[j] = temp # A posição inicial receberá o menor valor.
        intervalo = intervalo // 2 # Irei dividir o intervalo várias vezes até que, no final, resulte um insertion sort.
    return arr_

print(f"SHELL SORT : {shell_sort([10, 95, 33, 1, 3, 4])}")




################### SHELL SORT OK.



def merge_sort(arr_ : list[int]) -> list[int]:
    if len(arr_) > 1: # Dividindo o array em parte da esquerda e parte da direita.
        div = len(arr_) // 2
        left = arr_[ : div].copy()
        right = arr_[div : ].copy()
        merge_sort(left) # Irei, recursivamente, quebrar todo o array para posições únicas.
        merge_sort(right)

    # Após quebrar todo o array em posições de direita e esquerda, irei juntar o array o ordenando.
        i = j = k = 0
        while (i < len(left) and j < len(right)):
            if left[i] > right[j]:
                arr_[k] = right[j]
                j += 1
            else:
                arr_[k] = left[i]
                i += 1
            k += 1 # O k terá de ser incrementado.

        while i < len(left):
            arr_[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr_[k] = right[j]
            j += 1
            k += 1
    return arr_

print(f"MERGE SORT : {merge_sort([10, 95, 33, 1, 3, 4])}")




# Quicksort

# Aqui estará a lógica de varrer o vetor e separá-los entre elementos maiores e menores do que o pivô.
def particao(arr_ : list[int], start, end) -> list[int]:
    pivo = arr_[end] # Escolhendo o pivo como o último elemento do array.
    i = start - 1

    for j in range(start, end): # Comparando todos os elementos.
        if arr_[j] <= pivo: # Toda vez que o pivo for maior, irei colocá-los no começo da lista.
            i += 1
            arr_[i], arr_[j] = arr_[j], arr_[i] # Realizando a troca.

    arr_[i + 1], arr_[end] = arr_[end], arr_[i + 1] # Passando o pivo para as posições iniciais.
    return i + 1 # Irei retornar o índice onde o atual pivo se encontra.

def quick_sort(arr_ : list[int], start, end) -> list[int]:
    if start < end: # Enquanto eu puder dividir.
        # Basicamente estou ordenando o vetor com a função partição, e retornando o índice onde o pivô fica.
        posicao = particao(arr_, start, end) # Pegarei toda hora a posição do elemento pivô.
        
    # A ideia agora, é que, através de recursão, irei ordenar a parte esquerda (menores valores) e também a parte direita.

        # Ordenando a parte esquerda.
        quick_sort(arr_, start, posicao - 1)

        # Ordenando a parte direita.
        quick_sort(arr_, posicao + 1, end)
    return arr_ # retornando o array ordenado.


arr = np.array([10, 95, 33, 1, 3, 4])

print(f"QUICK SORT : {quick_sort(arr, 0, len(arr) - 1)}")