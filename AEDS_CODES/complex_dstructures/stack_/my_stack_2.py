from node_file import Node

# Inserir, remover e observar
class Stack:

    # O(1)
    def __init__(self): # Inicializando a lista como nula.
        # Aponta para o inicio da lista.
        self.topo = None 
        self._size = 0

    # O(1)
    def __len__(self): # Essa é 1 função especial em python.
        ''' Retorna o tamanho da lista encadeada
        '''
        return self._size 
    
    # O(1)
    def push(self, value : int):
        if self._size == 0:
            print("Criando a pilha.")
        node = Node(value) 
        node.next_ = self.topo # Ligando o novo elemento aos elementos anteriores da pilha.
        self.topo = node # Agora temos 1 novo topo.
        self._size = self._size + 1

    # O(1)
    def pop(self):
        if self._size == 0:
            raise Exception(" Nao há o que remover, a lista já está vazia.")
        else:
            node = self.topo # Pegando o nó do topo.
            self.topo = self.topo.next_ # Irá apontar para o None.
            self._size = self._size - 1
            return node.value_
        
    # O(1)
    def peek(self):
        if self._size > 0 :
            return self.topo.value_
        raise IndexError("A pilha está vazia.")
    
    # O(1)
    def __repr__(self):
        r = ""
        pointer = self.topo
        while(pointer):
            r = r + str(pointer.value_) + "\n"
            pointer = pointer.next_
        return r

    # O(1)         
    def __str__(self):
        return self.__repr__()