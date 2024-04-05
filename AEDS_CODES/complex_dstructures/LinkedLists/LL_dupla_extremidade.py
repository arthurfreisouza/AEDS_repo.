from class_NO import Node

class LL_duple:
    def __init__(self, max : int = 10):
        self.inicio = None
        self.final = None
        self.max_size = max
        self.actual_size = 0

    def isEmpty(self):
        return (self.inicio == None)
    
    def isFull(self):
        return (self.actual_size == self.max_size)
    
    def inserir_inicio(self, value : int):
        my_node = Node(value)
        if self.isEmpty():
            print("Criando a lista ...")
            self.inicio = my_node
            self.final = my_node
        else:
            my_node.next_ = self.inicio
            self.inicio = my_node
        self.actual_size += 1

    def mostrar(self) -> None:
        if self.isEmpty():
            print(" A lista está vazia...")
            return
        else:
            pointer = self.inicio
            while (pointer != None):
                print(pointer.show_value())
                pointer = pointer.next_


    def inserir_final(self, value):
        my_node = Node(value)
        if self.isEmpty():
            self.inicio = my_node
            self.final = my_node
        elif self.isFull():
            raise Exception(" The list already is full...")
        else:
            self.final.next_ = my_node
            self.final = my_node
        self.actual_size += 1
        return self.final.value_
        
    def excluir_inicio(self):
        if self.isEmpty():
            raise Exception(" The list already is empty...")
        else:
            temp = self.inicio.value_
            self.inicio = self.inicio.next_
            if self.inicio == None:
                self.final = None
        return temp