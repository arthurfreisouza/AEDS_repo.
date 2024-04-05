import numpy as np

# O case break é quando os vetores divididos sao menores ou iguais a 1, ou seja, quando tenho apenas elementos individuais.
def merge_sort(vector : list[int]) -> list[int]:
    if len(vector) > 1:
        division = len(vector) // 2
        left = vector[ : division].copy()
        right = vector[division : ].copy()
    merge_sort(left)
    merge_sort(right)

    # Acima está toda a parte de divisão do vetor, que será realizada com recursão
    i = j = k = 0
    # Para ordenar os elementos a esquerda e a direita.
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            vector[k] = left[i]
            i += 1
        else:
            vector[k] = right[j]
            j += 1
        k += 1

    # Pegando os elementos restantes que não foram alocados no vetor resultante.
    while i < len(left):
        vector[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        vector[k] = right[j]
        j += 1
        k += 1
    return vector
     














def mergesort2(list, begin = 0, end = None):
    if end is None:
        end = len(list)
    if (end - begin > 1):
        half = (begin + end) // 2
        # Irei dividir ambas as listas através de recursão e, quando ela ja estiver toda dividida, irei ter a variável half.
        # Irei chamar a função merge quando a lista estiver toda dividida.
        mergesort2(list, begin, half)
        mergesort2(list, half, end)
        merge(list, begin, half, end)

# A função merge irá fazer o papel de ordenar toda a lista.
def merge(list, begin, half, end):
    left = list[begin : half]
    right = list[half : end]
    top_left_, top_right_ = 0, 0
    for k in range(begin, end):
        if top_left_ >= len(left): # Caso a lista da esquerda já tenha extrapolado todos os valores que a contém, irei usar apenas os valores da lista da direita.
            list[k] = right[top_right_]
            top_right_ = top_right_ + 1

        elif top_right_ >= len(right): # Caso a lista da direita já tenha extrapolado todos os valores que a contém, irei usar apenas os valores da lista da esquerda.
            list[k] = left[top_left_]
            top_left_ = top_left_ + 1

        elif left[top_left_] < right[top_right_]: # Irei comparar os valores na posição das 2 listas.
            list[k] = left[top_left_]
            top_left_ += 1
        else:
            list[k] = right[top_right_]
            top_right_ += 1

mergesort2([3, 2, 5])
          