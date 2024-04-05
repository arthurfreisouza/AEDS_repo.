def insertion_sort(vector : list[int]) -> list[int]:
    size = len(vector)
    for i in range(1, size):
        elem_highlighted  = vector[i] # Toda hora 1 elemento será marcado, e o que estiver a sua esquerda estará ordenado.

        previous = i - 1 # Todos os elementos a esquerda do elemento marcado estará representado pela variável previous.
        
        while (previous >= 0 and elem_highlighted < vector[previous]): # Enquanto houver indice e o elemento marcado for menor...
            vector[previous + 1] = vector[previous] # Deslocando...
            previous -= 1
        vector[previous + 1] = elem_highlighted # Encaixando o elemento na posição desejada...
    
    return vector