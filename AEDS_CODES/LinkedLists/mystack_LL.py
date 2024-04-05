class Node:
    def __init__(self, value : int):
        #self.previous_ = None
        self.next_ = None
        self.value_ = value

    def show_value(self):
        print(self.value_)

class stack:
    def __init__(self, max_size : int = 10):
        self.head_ = None
        self.max_size_ = max_size # Tamanho máximo da lista.
        #self.last_ = None
        self.actual_size_ = 0

    def isEmpty(self):
        return (self.actual_size_ == 0)
    
    def __isFull(self):
        return (self.actual_size_ == self.max_size_)
    
    def __len__(self):
        return (self.actual_size_)
    
    def empilhar(self, value : int):
        new_node = Node(value)
        if self.isEmpty():
            self.head_ = new_node
        else:
            pointer = self.head_
            while(pointer.next_ != None):
                pointer = pointer.next_
            pointer.next_ = new_node

        self.actual_size_ += 1

    def desempilhar(self):
        if self.isEmpty():
            raise Exception("A lista está vazia...")
        else:
            pointer = self.head_
            while (pointer.next_ != None):
                anterior = pointer
                pointer = pointer.next_
            anterior.next_ = None
        self.actual_size_ -= 1

    def ver_topo(self):
        if self.isEmpty():
            return None
        else:
            pointer = self.head_
            while (pointer.next_ != None):
                pointer = pointer.next_         
        return pointer.value_
    
    def show_values(self):
        pointer = self.head_
        while (pointer != None):
            pointer.show_value()
            pointer = pointer.next_
