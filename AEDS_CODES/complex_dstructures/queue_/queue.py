# CRIAR 1 FILA CIRCULAR
# FUNCAO PARA VERIFICAR SE ESTA VAZIA OU CHEIA
# FUNCAO PARA ENFILEIRAR ()


import numpy as np

class row:
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

    def inserir(self, value):
        if self.isFull(): # Caso a fila esteja cheia...
            print("Está cheia")
            raise Exception(" Você não pode inserir um valor.")
    
        # Caso esteja na última posição da fila, volte para a primeira (a mais antiga que entrou na fila).
        if (self.last_pos == self.size_ - 1):
            self.last_pos = -1
        self.quantidade_el += 1
        self.last_pos += 1
        self.valores[self.last_pos] = value

    def remover(self):
        if self.isEmpty(): # Verificando se a lista está vazia...
            print("Está vazia.")
            raise Exception("A fila já está vazia.")
        temp = self.valores[self.inicial] # Pegando a variável que será retornada na hora de remover.
        if self.inicial == self.size_: # Caso eu já tenha removido os N valores da lista, irei ter que voltar da posição 0 para remover os novos mais recentes.
            self.inicial = 0
        self.quantidade_el -= 1
        self.inicial += 1
        return temp # retornando o primeiro elemento da lista.
    

    def primeiro(self):
        if self.isEmpty():
            print("Está vazia.")
        else:
            return(self.valores[self.inicial])
        


