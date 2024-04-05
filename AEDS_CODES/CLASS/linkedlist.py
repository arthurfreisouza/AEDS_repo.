from node_file import Node

class LinkedList:
    def __init__(self): # Inicializando a lista como nula.
        # Aponta para o inicio da lista.
        self.head = None 
        self._size = 0


    def append(self, value):
# Pegarei 1 ponteiro que irá percorrer a lista até o final.
# Ao chegar ao final, irei criar 1 novo nó.
        if self.head:
            pointer = self.head
            while (pointer.next_):
                pointer = pointer.next_
            pointer.next_ = Node(value)
        else:
            self.head = Node(value)
# Tenho que acrescentar a variável size.
        self._size += 1

    def __len__(self):
        ''' Retorna o tamanho da lista encadeada
        '''
        return self._size 
    
    def __getitem__(self, index):
        pointer = self._getnode(index)
        if pointer:
            return pointer.value_
        else:
            raise IndexError("list index out of range")
    
    def __setitem__(self, index, value):
        pointer = self._getnode(index)
        if pointer:
            pointer.value_ = value
        else:
            raise IndexError("list index out of range")

    def _getnode(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next_
            else:
                raise IndexError("list index out of range")
        
        return pointer


    def index(self, value_):
        ''' Retorna o indice do elemento na lista.
        '''
        i = 0 
        pointer = self.head
        while(pointer):
            if pointer.value_ == value_:
                return i
            pointer = pointer.next_
            i += 1
        raise ValueError("{} is nos in the list".format(value_))     
    
    def insert(self, index, value):
        node = Node(value)
        if index == 0:
            node.next_ = self.head
            self.head = node
        else:
            pointer = self._getnode(index - 1)
            node.next_ = pointer.next_
            pointer.next_ = node
        self._size += 1

    def remove(self, value):
        if self.head.value_ == value:
            self.head = self.head.next_
        else:
            pointer = self.head
            while pointer:
                if pointer.value_ == value:
                    aux = last_index
                    pointer = last_index
                    

                    pass
                else:
                    last_index = pointer.next_ 
             