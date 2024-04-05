import numpy as np

class Deque:
    def __init__(self, size : int) :
        self.size_ = size
        self.last_pos = 0
        self.quantidade_el = 0
        self.inicial = -1
        self.valores = np.empty(self.size_, dtype = int) # Criando 1 array com os valores vazios.


    def __deque_cheio(self):
        return (self.inicial == 0 and self.last_pos == (self.size_ -1 )) or (self.inicial == (self.last_pos + 1))
    
    def __deque_vazio(self):
        return self.quantidade_el == 0

    def __len__(self):
        return self.quantidade_el
    

    def insere_inicio(self, value):
        if self.__deque_cheio(): # Verificando se a deque já está cheia.
            print(" O deque está cheio")
            return
        
        if self.inicial == -1: # Caso ela esteja no início, tanto o inicio quanto o final apontarão para o mesmo valor...
            self.inicial = 0
            self.last_pos = 0

        elif self.inicial == 0:
            self.inicial = self.size_ - 1
        else:
            self.inicial -= 1

        self.quantidade_el += 1
        self.valores[self.inicial] = value

    
    def insere_final(self, value):
        if self.__deque_cheio():
            print("O deque está cheio ")
            return

        if self.inicial == -1:
            self.inicial = 0
            self.last_pos = 0

        elif self.last_pos == self.size_ - 1:
            self.last_pos = 0
        else:
            self.last_pos += 1

        self.quantidade_el += 1
        self.valores[self.last_pos] = value

    def excluir_inicio(self):
        if self.__deque_vazio():
            print("O deque já está vazio.")
            return
        # Possui somente 1 elemento
        if self.inicial == self.last_pos:
            self.inicial = -1
            self.last_pos = -1
        else:
            if self.inicial == self.size_ -1:
                self.inicial = 0
            else:
                self.inicial += 1
                self.quantidade_el -= 1

    def excluir_final(self):
        if self.__deque_vazio():
            print("O deque já está vazio.")
            return
        
        if self.inicial == self.last_pos:
            self.inicial = -1
            self.last_pos = -1
        elif self.inicial == 0:
            self.final = self.last_pos -1
        else:
            self.last_pos -= 1
            self.quantidade_el -= 1

    def get_inicio(self):
        if self.__deque_vazio():
            print("O deque está vazio")
            return 
        return self.valores[self.inicial]
    
    def get_final(self):
        if self.__deque_vazio():
            print("O deque está vazio")
            return 
        return self.valores[self.last_pos]
    

deque = Deque(5)

deque.insere_final(5)
deque.insere_final(10)
deque.insere_inicio(3)
deque.insere_inicio(2)
deque.insere_final(11)

deque.insere_inicio(43)

print(deque)
deque.excluir_inicio()
deque.excluir_final()