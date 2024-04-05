class Node:
    def __init__(self, value : int):
        self.value_ = value
        self.anterior = None
        self.proximo = None

    def show_value(self):
        return self.value_

class ListaDuplamenteEncadeada:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def __isEmpty(self):
        return (self.primeiro == None)
    
    def insere_inicio(self, value):
        my_node = Node(value)
        if self.__isEmpty():
            self.ultimo = my_node
        else:
            self.primeiro.anterior = my_node
        my_node.proximo = self.primeiro
        self.primeiro = my_node

    def insere_final(self, value):
        my_node = Node(value)
        if self.__isEmpty():
            self.primeiro = my_node
        else:
            self.ultimo.proximo = my_node
        my_node.anterior = self.ultimo
        self.ultimo = my_node   
    
    def mostrar_frente(self):
        pointer = self.primeiro
        while pointer != None:
            print(pointer.show_value())
            pointer = pointer.proximo

    def mostrar_atras(self):
        pointer = self.ultimo
        while pointer != None:
            print(pointer.show_value())
            pointer = pointer.anterior
            
    def excluir_inicio(self):
        temp = self.primeiro
        if self.primeiro.proximo == None:
            self.ultimo = None
        else:
            self.primeiro.proximo.anterior = None
        self.primeiro = self.primeiro.proximo
        return temp
    
    def excluir_final(self):
        temp = self.ultimo
        if self.primeiro.proximo == None:
            self.primeiro = None
        else:
            self.ultimo.anterior.proximo = None
        self.ultimo = self.ultimo.anterior
        return temp
    
    def excluir_posicao(self, value):
        pointer = self.primeiro
        while pointer.value_ != value:
            pointer = pointer.proximo
            if pointer == None:
                return None
        if pointer == self.primeiro:
            self.primeiro = pointer.proximo
        else:
            pointer.anterior.proximo = pointer.proximo
            #pointer.proximo.anterior = pointer.anterior
        
        if pointer == self.ultimo:
            self.ultimo = pointer.anterior
        else:
            pointer.proximo.anterior = pointer.anterior

        return pointer.value_