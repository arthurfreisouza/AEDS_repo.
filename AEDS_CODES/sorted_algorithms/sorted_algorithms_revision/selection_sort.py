import random

random_numbers = []
for i in range(20):
    random_numbers.append(random.randint(0, 100000))

# Irei percorrer todo o array, e colocarei os valores minimos na frente através de 1 variável auxiliar min.
def selection_sort(arr_ : list[int]):
    size_arr = len(arr_)

    for i in range(size_arr): # A cada iteração de i, os menores valores serão passados para a posição inicial.
        min = i
        for j in range(i + 1, size_arr): # Todos os elementos antes de i são ordenados.
            if arr_[min] > arr_[j]:
                min = j # Faço bem menos comparações do que o bubble sort.
        temp = arr_[i]
        arr_[i] = arr_[min]
        arr_[min] = temp
    return arr_


#print(selection_sort(random_numbers))






print(random_numbers)

def selection_recursive(arr_ : list[int]) -> list[int]:

    if len(arr_) == 1: # A cada iteração irei diminuir o tamanho do arr que passo de parâmetro para a função, quando chegar em 1 estará tudo ordenado.
        return arr_
    
    min_index = 0
    for i in range(1, len(arr_)):
        if arr_[min_index] > arr_[i]:
            min_index = i
    
    temp = arr_[0]
    arr_[0] = arr_[min_index]
    arr_[min_index] = temp

    return [arr_[0]] + selection_recursive(arr_[1 : ])

print(selection_recursive(random_numbers))