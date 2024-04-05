# A ideia é que a variável min irá armazenar, sempre, o menor valor da lista e irá passá-la para a primeira posição livre da lista.
def selection_sort_it(vector : list[int]) -> list:
    min = None
    for i in range(len(vector)):
        min = i
        for j in range(i + 1, len(vector)): # Começarei a analisar após a variável i que já está na posição correta.
            if vector[min] > vector[j]:
                min = j
        temp = vector[i]
        vector[i] = vector[min]
        vector[min] = temp
    return vector

