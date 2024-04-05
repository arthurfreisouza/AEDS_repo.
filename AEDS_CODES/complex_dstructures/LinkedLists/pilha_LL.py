from Node1 import Node

class stack:
    def __init__(self, max_size : int = 5):
        self.head = None
        self.max_size_ = max_size
        self.actual_size_ = 0

    def isEmpty(self):
        return (self.actual_size_ == 0)
    
    def isFull(self):
        return (self.actual_size_ == self.max_size_)

    def __len__(self):
        return (self.actual_size_)
    
    def Empilhar(self, value : int):
        new_node = Node(value)
        if self.isFull():
            print(" The stack already is fully...")
            return None
        if self.isEmpty():
            self.head = new_node
        else:
            pointer = self.head
            while (pointer.next_ != None):
                pointer = pointer.next_
            pointer.next_ = new_node
        self.actual_size_ += 1

    
    def Desempilhar(self) -> int:
        if self.head.next_ == None:
            temp = self.head.value_
            self.head = None
            return temp
        if self.isEmpty():
            raise Exception(" A lista já está vazia...")
        pointer = self.head
        while (pointer.next_ != None):
            anterior = pointer
            pointer = pointer.next_
        temp = pointer.value_
        anterior.next_ = pointer.next_
        self.actual_size_ -= 1
        return temp
    
    def ver_topo(self):
        if self.isEmpty():
            print(" A lista já está vazia...")
            return None
        else:
            pointer = self.head
            while (pointer.next_ != None):
                pointer = pointer.next_
            return pointer.value_
    
    def ver_pilha(self):
        if self.isEmpty():
            print("A pilha está vazia; ...")
            return None
        else:
            pointer = self.head
            while (pointer != None):
                print(pointer.show_value())
                pointer = pointer.next_

            
#stack_LL = stack()
#stack_LL.Empilhar(1)
#stack.isEmpty()
#print(stack.ver_topo())