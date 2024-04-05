import numpy as np

class FilaPrioridade:
    def __init__(self, size : int) :
        self.size_ = size
        self.last_pos = -1
        self.quantidade_el = 0
        self.inicial = 0
        self.valores = np.empty(self.size_, dtype = int) # Criando 1 array com os valores vazios.

    def isEmpty(self): # Para verificar se a fila está vazia.
        return (self.last_pos == -1)

    def isFull(self): # Para verificar se a fila está cheia.
        return (self.quantidade_el == self.size_)
    

    def enfileirar(self, value):
        if self.isFull():
            print("A fila está cheia")
            return
        if self.isEmpty():
            self.valores[self.quantidade_el] = value
            self.last_pos += 1
            self.quantidade_el += 1
        else:
            x = self.quantidade_el - 1 # Começarei a percorrer o vetor, ele será ordenado da direita para a esquerda.
            while x >= 0:
                if value > self.valores[x]: # [6, 5, 4] => 7 =>[7, 6, 5, 4]
                    self.valores[x + 1] = self.valores[x]
                else:
                    break
                x -= 1
            self.valores[x + 1] = value
            self.quantidade_el += 1

    def desinfileirar(self):
        if self.isEmpty():
            print("Está vazia")
            return
        valor = self.valores[self.inicial]
        self.quantidade_el -= 1
        return valor
    

    def primeiro(self):
        if self.isEmpty():
            print("Está vazia.")
        else:
            return(self.valores[self.inicial])
        

fila = FilaPrioridade(5)
fila.enfileirar(30)
fila.enfileirar(50)
fila.enfileirar(10)
fila.enfileirar(40)
fila.enfileirar(20)
fila.desinfileirar()
fila.desinfileirar()
fila.desinfileirar()
fila.enfileirar(5)
        