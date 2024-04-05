# Criando a classe Nó
class Node:
    def __init__(self, value : int):
        self.value_ = value
        self.next_ = None # O próximo valor da lista encadeada.
        self.previous_ = None # O valor anterior da lista encadeada.

    def show_value(self) -> None:
        print(self.value_)

class ListaDuplamenteEncadeada:
    def __init__(self, size : int = 5) -> None:
        self.first_ = None
        self.last_ = None
        self.max_size_ = size
        self.actual_size_ = 0
    
    def __len__(self): # Retorna o tamanho da lista encadeada.
        return self.actual_size_
    
    def isEmpty(self): # Retorna se a lista encadeada está vazia.
        return (self.actual_size_ == 0)
    
    def isFull(self): # Retorna se a lista encadeada está cheia.
        return (self.actual_size_ == self.max_size_)
    
    # O raciocínio para inserir no início e inserir no final são análogos.
    # Para entender, basta desenhar 1 lista encadeada.
    def insert_in_begin(self, value : int) -> None:
        new_node = Node(value)
        if self.isFull():
            raise Exception(" The list is fully.")
        if self.isEmpty():
            self.last_ = new_node
        else:
            self.first_.previous_ = new_node
        new_node.next_ = self.first_
        self.first_ = new_node
        self.actual_size_ += 1
    
    def insert_in_final(self, value : int) -> None:
        new_node = Node(value)
        if self.isFull():
            raise Exception(" The list is fully.")
        if self.isEmpty():
            self.first_ = new_node
        else:
            self.last_.next_ = new_node
        new_node.previous_ = self.last_
        self.last_ = new_node
        self.actual_size_ += 1
    
    def show_first(self):
        if self.actual_size_ == 0:
            print(" The list is empty")
            return
        pointer = self.first_
        while (pointer != None):
            pointer.show_value()
            pointer = pointer.next_
    
    def show_last(self):
        if self.actual_size_ == 0:
            print(" The list is empty")
            return
        pointer = self.last_
        while (pointer != None):
            pointer.show_value()
            pointer = pointer.previous_

    def exclude_in_begin(self):
        temp = self.first_.value_
        if self.first_.next_ == None:
            self.last_ = None
        else:
            self.first_.next_.previous_ = None
        self.first_ = self.first_.next_
        self.actual_size_ -= 1
        return temp

    def exclude_in_final(self):
        temp = self.last_.value_
        if self.first_.next_ == None:
            self.first_ = None
        else:
            self.last_.previous_.next_ = None
        self.last_ = self.last_.previous_
        self.actual_size_ -= 1
        return temp
            
    def exclude_value(self, value):
        pointer = self.first_
        while (pointer.value_ != value):
            pointer = pointer.next_
            if pointer == None: # Significa que não achou o valor.
                return None
        if pointer == self.first_:
            self.first_ = self.first_.next_
        else:
            pointer.previous_.next_ = pointer.next_

        if pointer == self.last_:
            self.last_ = self.last_.previous_
        else:
            pointer.next_.previous_ = pointer.previous_
        
        self.actual_size_ -= 1
        return pointer.value_
            


