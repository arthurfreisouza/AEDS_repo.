from Node import Node

class LinkedList:
    def __init__(self, max = 5): # Inicializando a lista encadeada.
        self.max_size_ = max
        self.actual_size_ = 0
        self.head = None


    def isEmpty(self): # Retornando se está vazia.
        return (self.actual_size_ == 0)
    

    def isFull(self): # Retornando se está cheia.
        return (self.actual_size_ == self.max_size_)
    

    def __len__(self):
        return self.actual_size_
    

    def append(self, value : int): # Realizando o append (adicionando no final da lista).
        my_node = Node(value)
        if self.isEmpty(): # Caso esteja vazia.
            my_node.next_ = self.head
            print("Criando a lista encadeada...")
            self.head = my_node

        elif self.isFull(): # Caso esteja cheia.
            raise IndexError(" Index out of range...")
        
        else: # Caso não esteja vazia nem cheia...
            pointer = self.head
            while (pointer.next_ != None): # O ponteiro irá percorrer toda a lista encadeada, até chegar ao final...
                pointer = pointer.next_
            pointer.next_ = my_node
        self.actual_size_ += 1 # Irei incrementar 1 valor no tamanho, visto que realizei o append.


    def imprime(self):
        if self.isEmpty():
            print("The list is empty ...")
        else:
            pointer = self.head
            while (pointer != None):
                print(pointer.show_value())
                pointer = pointer.next_


    def pegando_index(self, value : int):
        count = 0 # A variável que iá contar em qual index estará o valor...
        pointer = self.head
        if self.isEmpty(): # Caso a lista esteja vazia, o retorno será none.
            print("A lista está vazia...")
            return None
        else: # Irei percorer toda a lista, enquanto o valor atual for diferente do valor desejado.
            while (pointer.value_ != value):
                pointer = pointer.next_
                count += 1
                if pointer == None: # Caso eu chegue ao final da lista (dado por none), irei lançar 1 exceção pois o valor não está na lista.
                    raise IndexError(" The value is not in the list...")
            return count # Caso eu ache o valor, o indice será retornado...


    def remover_final(self):
        if self.isEmpty(): # Verificando se a lista está vazia...
            print(" The list is empty ...")
            return None
        else:
            pointer = self.head
            while(pointer.next_ != None):
                anterior = pointer # O anterior sempre terá o elemento anterior, ao atual.
                pointer = pointer.next_
            temp = pointer.value_
            anterior.next_ = pointer.next_ # Agora, o anterior.next nao irá apontar para 1 elemento, e sim para o none, perdendo a conexão da lista encadeada.
            self.actual_size_ -= 1
            return temp


    def remover(self, value : int):
        pointer = self.head
        if self.isEmpty(): # Analisando se a lista está vazia...
            print(" The list is Empty...")
            return None
        elif pointer.value_ == value: # Caso on primeiro elemento seja o valor desejado...
            temp = pointer.value_
            self.head = pointer.next_
        else: # Irei pegar o index do valor que quero remover, ir para 1 posição antes, salvar o valor a ser removido, e apontar o elemento anterior para o elemento próximo.
            idx = self.pegando_index(value) # Pegando o index de onde está o valor que eu quero.
            for i in range(idx):
                anterior = pointer
                pointer = pointer.next_
            temp = pointer.value_
            anterior.next_ = pointer.next_
        self.actual_size_ -= 1
        return temp
    

    def inserir_posicao(self, idx : int, value : int):
        my_node = Node(value) # Criando o nó contendo o valor desejado.
        pointer = self.head 
        if self.isEmpty():
            print("The list is empty ...")
            self.head = my_node

        else:
            for i in range(idx): # Irei varrer todo o array até a posição desejada.
                anterior = pointer
                pointer = pointer.next_
            my_node.next_ = pointer    
            anterior.next_ = my_node # Para inserir, basta apenas fazer o elemento anterior apontar para o elemento atual, e o atual para o próximo.

        self.actual_size_ += 1
        return my_node.value_

    def get_node(self, index):
        pointer = self.head
        for i in range(index):
            if pointer != None:
                pointer = pointer.next_
            else:
                raise IndexError("list index out of range...")
        return pointer
            

    def __getitem__(self, index : int):
        pointer = self.get_node(index)
        return pointer.value_
    
    def __setitem__(self, index : int, value : int):
        pointer = self.get_node(index)
        pointer.value_ = value

            
        

            
