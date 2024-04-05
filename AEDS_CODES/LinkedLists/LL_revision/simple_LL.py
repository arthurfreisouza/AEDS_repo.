class Node:
    def __init__(self, name : str): # A lista encadeada recebe 1 nome.
        self.next_ = None
        self.name_ = name

    def show_names(self) -> None:
        print(self.name_)
    
class Linked_List:
    def __init__(self, max_size : int = 10) -> None: # Criando a  lista encadeada, ela inicia com 1 tamanho nulo.
        self.head_ = None
        self.max_size_ = max_size
        self.actual_size_ = 0
    
    def is_Empty(self): # Retorna se a lista está vazia.
        return (self.actual_size_ == 0)
    
    def is_Full(self): # Retorna se a lista está cheia.
        return (self.actual_size_ == self.max_size_)
    
    def __len__(self): # Funções desse tipo são consideradas especiais em python.
        return (self.actual_size_)
    
    def insert_in_begin(self, name_ : str):
        new_node = Node(name_)
        if self.is_Empty():
            self.head_ = new_node
            print("Creating the list")

        elif self.is_Full():
            raise Exception(" The list already is full...")
        else:
            new_node.next_ = self.head_ # Agora o novo elemento apontará para o antigo primeiro elemento.
            self.head_ = new_node # Agora a referência para o primeiro elemento está apontando para o novo elemento.
            print("Sucessfull insertion")
        self.actual_size_ += 1

    def insert_in_final(self, name_ : str):
        new_node = Node(name_)
        if self.is_Empty():
            self.head_ = new_node
            print("Creating the list")
        elif self.is_Full():
            raise Exception(" The list already is full...")
        else:
            pointer = self.head_
            while pointer.next_ != None: # O pointer irá percorrer até o último elemento, onde irá armazenar o novo elemento da lista.
                pointer = pointer.next_
            pointer.next_ = new_node
            print("Sucessfull insertion")
        self.actual_size_ += 1 # Aumentando o tamanho da lista.

    def insert_in_pos(self, name_ : str, index_ : int):
        new_node = Node(name_)
        if self.is_Empty():
            self.head_ = new_node
            print("Creating the list")
        elif self.is_Full():
            raise Exception(" The list already is full...")
        else:
            actual_position = self.head_
            previous_position = None # Conterá o valor anterior
            for i in range(index_): # Varrendo a lista até o indice atual, onde irei fazer o anterior apontar para o próximo e esquecer o índice atual.
                previous_position = actual_position
                actual_position = actual_position.next_
            new_node.next_ = actual_position
            previous_position.next_ = new_node
            print("Sucessfull insertion")
        self.actual_size_ += 1 # Aumentando o tamanho da lista.

    def remove_in_begin_(self) -> str:
        if self.is_Empty():
            raise Exception(" The list already is empty...")
        else:
            temp = self.head_.name_ # Pegando a variável inicial que será removida.
            self.head_ = self.head_.next_
            print("Sucessfull remotion")
        self.actual_size_ -= 1 # Reduzindo o tamanho da lista.
        return temp

    def remove_in_final(self) -> str:
        if self.is_Empty():
            raise Exception("The list already is empty...")
        else:
            pointer = self.head_
            while pointer.next_.next_ != None: # Percorrerei até 1 posição anterior ao último elemento. [1] -> [2] -> *[3] -> [4] -> NULL
                pointer = pointer.next_
            temp = pointer.next_.name_ # Pegando o nome do último elementod a lista.
            pointer.next_ = None # Excluindo a ligação entre o penúltimo e o último, ou seja, excluindo o último elemento.
        self.actual_size_ -= 1 # Reduzindo o tamanho da lista.
        return temp

    def remove_element(self, element_ : str) -> str:
        if self.is_Empty():
            raise Exception(" The list is empty ...")
        else:
            pointer = self.head_
            previous = None
            while pointer.name_ != element_: # Procurando o último elemento a ser removido.
                previous = pointer # Irá marcar o elemento anterior a elemento que quero remover.
                pointer = pointer.next_
            temp = pointer.name_ # Pegando o elemento que quero remover.
            previous.next_ = pointer.next_
        self.actual_size_ -= 1
        return temp
            
    def show_list_of_names(self):
        if self.is_Empty():
            raise Exception(" The list is empty ...")
        else:
            pointer = self.head_
            while pointer != None: # Varrendo toda a lista, inclusive o último elemento e imprimindo todos.
                pointer.show_names()
                pointer = pointer.next_