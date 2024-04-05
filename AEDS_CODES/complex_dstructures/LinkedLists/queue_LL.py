class Node:
    def __init__(self, value : int):
        self.next_ = None
        self.value_ = value

    def show_value(self):
        print(self.value_)


class queue:
    def __init__(self, max_size : int = 10):
        self.max_size_ = max_size
        self.head_ = None
        self.actual_size_ = 0
    
    def isEmpty(self):
        return (self.actual_size_ == 0)

    def isFull(self):
        return (self.actual_size_ == self.max_size_)

    def __len__(self):
        return (self.actual_size_)
    

    def enfileirar(self, value : int):
        new_node = Node(value)
        if self.isEmpty():
            self.head_ = new_node
        elif self.isFull():
            raise Exception(" The list already is full ...")
        else:
            pointer = self.head_

            while (pointer.next_ != None):
                pointer = pointer.next_
            pointer.next_ = new_node
        self.actual_size_ += 1

    def desinfileirar(self):
        if self.isEmpty():
            raise Exception(" The list already is empty ...")
        else:
            self.head_ = self.head_.next_
            self.actual_size_ -= 1

    def ver_inicio(self):
        if self.isEmpty():
            raise Exception(" The list is empty ...")
        else:
            print(self.head_.value_)

    def ver_final(self):
        if self.isEmpty():
            raise Exception(" The list is empty ...")
        else:
            pointer = self.head_
            while (pointer.next_ != None):
                pointer = pointer.next_
            return pointer.value_

    def show_values(self):
        if self.isEmpty():
            raise Exception(" The list already is empty ...")
        else:
            pointer = self.head_

            while (pointer != None):
                pointer.show_value()
                pointer = pointer.next_

            #while (pointer.next_ != None):
            #   pointer.show_value()
            #   pointer = pointer.next_
            #pointer.show_value()