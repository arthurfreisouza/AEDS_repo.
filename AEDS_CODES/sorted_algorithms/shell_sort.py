def shell_sort(vector : list[int]) -> list[int]:
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
                
