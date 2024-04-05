import numpy as np

class VetorOrdenado:
    # Ao criar o vetor apenas que tenho que definir sua capacidade.
    def __init__(self, capacidade):
        self.capacidade_ = capacidade
        self.ultima_pos = -1
        self.valores = np.empty(self.capacidade_, dtype = int) # Criando 1 vetor de N posições com todas elas sendo vazias.


    # O(n)
    def imprime(self):
        if self.ultima_pos == -1: # Caso o vetor esteja vazio.
            print(" Está vazio.")
        else:
            for i in range(self.ultima_pos + 1): # Imprimindo todas as posições...
                print(i, " - ", self.valores[i])

    # O(n)
    def insere(self, value_to_insert : int):
        if self.ultima_pos == self.capacidade_ - 1: # Caso o vetor esteja cheio...
            print(" Está cheio !")
            raise Exception ("Está cheio")
        
        posicao = 0
        for i in range(self.ultima_pos + 1):
            posicao = i
            if self.valores[i] > value_to_insert:
                break
            if i == self.ultima_pos:
                posicao = i + 1
        
        x = self.ultima_pos
        while x >= posicao: # Sairá da ultima posição, puxando elas mais afrente no vetor.
            self.valores[x + 1] = self.valores[x]
            x = x - 1
        self.valores[posicao] = value_to_insert
        self.ultima_pos = self.ultima_pos + 1


    def pesquisa_linear(self, value):
        for i in range(self.ultima_pos + 1):
            if self.valores[i] > value: # Irá parar quando encontrar algum valor da lista maior do que o valor desejado. 3     [ 1 2 4 6]
                return -1
            if self.valores[i] == value:
                return i
            if i == self.ultima_pos:
                return -1

    def pesquisa_binaria(self, value):
        inicial = 0
        final = self.ultima_pos
        while True:
            pos = int((inicial + final) / 2) # Definindo a posição que situa na metade da lista a ser aplicada a busca binária.
            if self.valores[pos] == value:
                return pos
            elif inicial > final: # O elemento não foi encontrado.
                return -1
            else:
                if self.valores[pos] < value: # Estará no extremo superior do vetor, então inicial = metade + 1
                    inicial = pos + 1
                else: # Estará no extremo inferior do vetor, então final = metade - 1
                    final = pos - 1

    def pesquisa_binaria_2(self, value, begin = 0, end = None):
        if end == None:
            end = len(self.valores) - 1
        if begin <= end:
            media_ = (begin + end) // 2
            if self.valores[media_] == value:
                return media_
            if value < self.valores[media_]:
                return self.pesquisa_binaria_2( value, begin, media_ -1)
            else:
                return self.pesquisa_binaria_2(value, media_ + 1, end) 
        return None


    def excluir(self, value):
        posicao = self.pesquisa_binaria(value) 
        if posicao == -1:
            return -1
        for i in range(posicao, self.ultima_pos):
            self.valores[i] = self.valores[i + 1]
        self.ultima_pos = self.ultima_pos - 1


vetor = VetorOrdenado(10)
vetor.insere(6)
vetor.insere(4)
vetor.insere(3)
vetor.insere(5)
vetor.insere(1)
vetor.insere(8)


vetor.pesquisa_binaria(3)
vetor.pesquisa_binaria_2(3)
