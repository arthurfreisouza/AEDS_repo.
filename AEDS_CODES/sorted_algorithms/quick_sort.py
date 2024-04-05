#def quick_sort(list, begin = 0, end = None):
#    if end is None:
#        end = len(list) - 1
#    if begin < end:
#        p = partition(list, begin, end)
#        quick_sort(list, begin, p - 1)
#        quick_sort(list, p + 1, end)
#
#def partition(list, begin, end):
#    pivot = list[end]
#    i = begin
#    for j in range(begin, end): # Barra rocha
#        if list[j] <= pivot:
#            list[j], list[i] = list[i], list[j]
#            i += 1
#        
#    list[i], list[end] = list[end], list[i]
#    return i
#
#
#quick_sort([7, 3, 10])


def particao(vector, begin, end):
    pivo = vector[end] # O pivô sempre será no final
    i = begin - 1 # Irá conter os valores que ficarão na esquerda (menores do que o pivô)

    for j in range(begin, end):
        if vector[j] <= pivo: # Os elementos menores que o pivô ficarão mais a esquerda
            i += 1 # Será incrementado apenas quando eu encontrar 1 elemento menor que o pivô. É usada para guardar o indice que marca os valores menores do que o pivô.
            vector[i], vector[j] = vector[j], vector[i] # Trocando os elementos menores do que o pivo.
        vector[i + 1], vector[end] = vector[end], vector[i + 1]
        return i + 1
    

def quick_sort(vector, begin, end):
    if begin < end:
        pos = particao(vector, begin, end)

        # Esquerda
        quick_sort(vector, begin, pos - 1)

        # Direita
        quick_sort(vector, pos + 1, end)

    return vector


quick_sort([1, 2, 3, 4, 5], 0, 4)