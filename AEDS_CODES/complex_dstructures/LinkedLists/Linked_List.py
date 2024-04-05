from class_NO import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def isEmpty(self):
        return (self.head == None)

    def inserir_inicio(self, value : int) -> int:
        my_node = Node(value)
        #my_node.next_ = self.head
        if self.isEmpty():
            print(f"Criando a lista encadeada...")
            self.head = my_node
        else:
            self.head = my_node
        self.size += 1
    
    def imprime(self) -> None:
        pointer = self.head
        while (pointer != None):
            print(pointer.show_value())
            pointer = pointer.next_

    def append(self, value : int):
        my_node = Node(value)
        if self.head:
            pointer = self.head
            while (pointer.next_ != None):
                pointer = pointer.next_
            pointer.next_ = my_node
        else:
            my_node.next_ = self.head
            self.head = my_node
        self.size += 1
    
    def remover_inicio(self):
        if self.isEmpty():
            print("A lista está vazia ...")
            return None
        temp = self.head.value_
        self.head = self.head.next_
        self.size -= 1
        return temp
    
    def procurar(self, value : int):
        if self.isEmpty():
            print("A lista está vazia ...")
            return None
        
        pointer = self.head
        count = 0
        while pointer.value_ != value:
            if pointer.next_ == None:
                return None
            else:
                pointer = pointer.next_
            count += 1
        return count
    
    def remover(self, value : int):
        atual = self.head
        anterior = self.head
        while atual.value_ != value:
            if atual.next_ == None:
                return None
            else:
                anterior = atual
                atual = atual.next_
        if atual == self.head:
            self.head = self.head.next_
        else:
            anterior.next_ = atual.next_
        self.size -= 1
        return atual.value_
         

