import numpy as np


class Stack:
    def __init__(self, cap_ : int = 10): # A capacidade será 10, caso nenhum valor seja passado.
        self.__capacidade = cap_
        self.__last_pos = -1
        self.__arr = np.empty(self.__capacidade, dtype = str) # Iniciando 1 array vazio.

    def push(self, value):
        if self.isFull(): # Caso o array esteja cheio : 
            raise Exception("Its full ! ")
        else:
            if self.isEmpty(): # Caso o array esteja vazio : 
                print("Creating the array ...")
            self.__last_pos = self.__last_pos + 1 # Posição inicial = -1, -1 + 1 = 0, então o primeiro elemento vai para a posição 0.
            self.__arr[self.__last_pos] = value

    def imprime(self): # Varrerá todo o array, imprimindo todos os valores...
        for i in range(self.__last_pos + 1):
            str_ = str(i) + " - " + str(self.__arr[i])
            print(str_)

    def ver_topo(self):
        if self.__last_pos == -1: # Caso o array esteja vazio.
            return -1
        else:
            return self.__arr[self.__last_pos]
    
    def pop(self):
        if self.isEmpty(): # Verifica se está vazio...
            raise Exception("Its empty ! ")
        else:
            self.__arr[self.__last_pos] = 0
            self.__last_pos = self.__last_pos - 1
    
    def peek(self): # Pega o topo da pilha.
        if self.__last_pos == -1:
            print("Pilha vazia..")
        else:
            return self.__arr[self.__last_pos]
    
    def isEmpty(self): # Ṕega se a pilha está vazia.
        cond = (self.__last_pos == -1)
        return cond == True
    
    def isFull(self): # Pega se a pilha está cheia.
        cond = (self.__last_pos == self.__capacidade - 1)
        return cond == True