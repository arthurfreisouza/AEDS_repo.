class Node:
    def __init__(self, value : int):
        self.value_ = value
        self.next_ = None
        self.previous_ = None

    def show_value(self):
        return (self.value_)
    

class ListaEncadeadaDupla:

    # Inicializando a lista encadeada.
    def __init__(self, max_size : int = 10):
        self.head_ = None
        self.last_ = None
        self.max_size_ = max_size
        self.actual_size_ = 0

    # As 3 funções mais básicas de lista encadeda.
    def __len__(self):
        return (self.actual_size_)
    
    def isEmpty(self):
        return (self.actual_size_ == 0)

    def isFull(self):
        return (self.actual_size_ == self.max_size_)
    


    def insert_on_begin(self, value : int):
        new_node = Node(value)
        if self.isEmpty():
            print("Creating the linked list ...")
            self.last_ = new_node # Eu só preciso mexer no final caso a lista esteja vazia.

        elif self.isFull():
            raise Exception("It's already full...")
        
        else:
            new_node.next_ = self.head_
            self.head_.previous_ = new_node
        self.actual_size_ += 1 # Adicionando 1 ao tamanho...
        self.head_ = new_node # Executarei esse comando independente se estiver vazia ou não

    def insert_on_final(self, value) -> None:
        new_node = Node(value)
        if self.isEmpty():
            self.head_ = new_node
        elif self.isFull():
            raise Exception("It's already full ...")
        else:
            new_node.previous_ = self.last_
            self.last_.next_ = new_node
        self.last_ = new_node
        self.actual_size_ += 1


    def show_begin(self) -> None:
        if self.isEmpty():
            raise Exception("The list is empty ...")
        else:
            pointer = self.head_
            while (pointer != None):
                print(pointer.show_value())
                pointer = pointer.next_

    def show_final(self) -> None:
        if self.isEmpty():
           raise Exception("The list is empty ...")
        else:
            pointer = self.last_
            while pointer != None:
                print(pointer.show_value())
                pointer = pointer.previous_

    def remove_begin(self):
        if self.actual_size_ == 1:
            self.head_ = None
            self.last_ = None
        if self.isEmpty():
            raise Exception("It's empty ...")
        else:
            self.head_.next_.previous_ = None
            self.head_ = self.head_.next_
            self.actual_size_ -= 1

    def remove_final(self):
        if self.actual_size_ == 1:
            self.head_ = None
            self.last_ = None
        if self.isEmpty():
            raise Exception("It's empty ...")
        else:
            self.last_.previous_.next_ = None
            self.last_ = self.last_.previous_
            self.actual_size_ -= 1