from node_file import Node

# Inserir, remover e observar
class Queue:

    # O(1)
    def __init__(self): # Na fila, irei inserir no final e retirar pessoas do começo.
        self.first = None
        self.last = None  
        self._size = 0

    # O(1)
    def __len__(self): # Essa é 1 função especial em python.
        ''' Retorna o tamanho da fila
        '''
        return self._size 
    
    # O(1)
    def push(self, value : int):
        node = Node(value)
        if self.last is None:
            self.last = node
        else:
            self.last.next_ = node
            self.last = node
        if self.first is None:
            self.first = node
        self._size += 1
        #node = Node(value)
        #if self._size == 0:
        #    self.first = node
        #    self.last = node
        #else:
        #    node.next_ = self.last
        #    self.last = node
        #self._size = self._size + 1

    # O(1)
    def pop(self):
        if self._size > 0:
            elem = self.first.value_
            self.first = self.first.next_
            self._size -= 1
            return elem
        raise IndexError(" A fila está vazia.")
        #if self._size == 0:
        #    raise Exception(" Nao há o que remover, a fila já está vazia.")
        #else:
        #    self.first = self.first.next_
        #self._size = self._size - 1
          
    # O(1)
    def peek(self):
        if self._size > 0 :
            return self.first.value_
        raise IndexError("A pilha está vazia.")
    
    # O(1)
    def __repr__(self):
        if self._size > 0:
            r = ""
            pointer = self.first
            while(pointer):
                r = r + str(pointer.value_) + " "
                pointer = pointer.next_
            return r
        return "Empty Queue"

    # O(1)         
    def __str__(self):
        return self.__repr__()