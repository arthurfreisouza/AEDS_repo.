'''def shell_sort(vector : list[int]) -> list[int]:
    intervalo = len(vector) // 2 # Pegando o ponto central de 1 vetor.


    while intervalo > 0: # Rodará enquanto eu puder dividir meu intervalo.
        for i in range(intervalo, len(vector)): # Irei varrer o vetor o qual eu dividi.
            temp = vector[i]
            j = i # Salvando a posição parar comparar os valores de cada intervalo.

            while j >= intervalo and vector[j - intervalo] > temp: # Entrará no loop enquanto der para trocar os valores
                vector[j] = vector[j - intervalo] # Comparando os valores de cada posicao nos 2 intervalos...
                j -= intervalo

            vector[j] = temp

        intervalo // 2 # Reduzindo o intervalo
    return vector



print(shell_sort([4, 2, 1, 8, 5, 3]))
'''


# Como pensar nesse algoritmo :

# Irei dividir semopre o número de intervalos pela metade. irei comparar as respectivas posições do array dividido.
# Quando a parte menor for maior do que os ultimos valores, irei realizar a troca.


def shell_sort(arr_ : list[int]) -> list[int]:
    intervalo = len(arr_) // 2 # O shell sort sempre trabalhará dividindo os intervalos.

    while intervalo > 0: # Enquanto eu puder dividir os intervalos, irei dividi-los e ordená-los.

        for i in range(intervalo, len(arr_)): # [4, 2, 1, *8, 5, 3]
            temp = arr_[i] # Variável temporária que irá pegar o valor da posição de index i (8).

            j = i # j terá o mesmo índice de i, que será i = j = 3.

            while j >= intervalo and arr_[j - intervalo] > temp: # Enquanto eu puder executar o loop (cond1) e a posição mais a esquerda for maior do que a posição mais a direita, irei trocar para ordenar.
                arr_[j] = arr_[j - intervalo] # Fazendo a troca e mandando a posição de maior valor para a posição mais a direita.
                j -= intervalo # Mudando o índice j para a posição que pegará o menor valor
            arr_[j] = temp # Agora, a menor posição receberá o menor valor.

        intervalo //= 2 # Reduzindo o intervalo
    
    return arr_ # Retornando o array ordenado.


print(shell_sort([4, 2, 1, 8, 5, 3]))