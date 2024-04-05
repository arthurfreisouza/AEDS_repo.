


def insertion_sort(arr_ : list[int]) -> list[int]:
    for i in range(1, len(arr_)):
        elem_highlighted = arr_[i] # Elemento que será comparado.
        previous = i -1 # Tudo que vem antes da posição marcada tem de estar ordenado...

        while previous >= 0 and elem_highlighted < arr_[previous]: # Enquanto os elementos comparados forem maiores do que o meu elemento marcado.
            arr_[previous + 1] = arr_[previous] # Irei deslocá-los todos para frente, o ponto que ele não encontrar elementos menores, ele estará na sua posição desejada, que será entre 1 numero maior e 1 menor do que ele.
            previous -= 1
        arr_[previous + 1] = elem_highlighted # Encaixando o elemento na posição desejada.

    return arr_ 