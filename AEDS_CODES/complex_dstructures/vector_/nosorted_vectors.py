import numpy as np

# Criação da classe vetor não ordenado.
class VetorNaoOrdenado():
    def __init__(self, size_ : int):
        self.size = size_
        self.last_pos = -1
        self.arr_ = np.empty(self.size, dtype = int) # Array numpy é menos custoso e mais eficiente.

    # 0(n)
    def print_values(self):
        if self.last_pos == -1: # A ultima posição ser -1 indica que está vazio.
            raise Exception ("Its wrong !")
        else:     
            for index in range(self.last_pos + 1): # Percorrendo todo o array e imprimindo os valores.    
                print(index, '-', self.arr_[index])

    # O(1)
    def size_f(self) -> int:
        return self.size
    
    # O(1)
    def insert(self, value : int):
        if self.last_pos == self.size - 1: # Caso o array esteja cheio...
            raise Exception("Capacidade máxima...")
        else:
            self.last_pos = self.last_pos + 1
            self.arr_[self.last_pos] = value # Caso não esteja cheio, irei inserir na última posição.
    # O(n)
    def search_(self, value):
        if self.last_pos == -1:
            raise Exception(" Its empty !")
        else:
            for i in range(self.last_pos + 1): # Percorrendo o array a procura do valor desejado, retornando o index desejado.
                if value == self.arr_[i]:
                    return i
            return -1 
        
    # O(n)
    def exclude(self, value):
        index_ = self.search_(value) # Pegando o índice do valor que quero excluir.
        if index_ == -1:
            return -1 # Caso não tenha o valor que quero excluir...
        else:
            for i in range(index_, self.last_pos): # Mudando o array todo de lugar a partir do indice excluido.
                self.arr_[i] = self.arr_[i + 1]
            self.last_pos = self.last_pos - 1


vector = VetorNaoOrdenado(10)

vector.insert(3)
vector.insert(2)
vector.insert(4)
vector.insert(5)
vector.insert(6)
vector.insert(1)

vector.print_values()


vector.search_(5)

vector.exclude(5)

vector.search_(5)
