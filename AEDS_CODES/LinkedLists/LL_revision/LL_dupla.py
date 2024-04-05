class Node:
    def __init__(self, value):
        self.value_ = value
        self.previous_ = None
        self.next_ = None
    
    def show_value(self) -> None:
        print(self.value_)

class Linked_List:
    def __init__(self, max_size : int = 5):
        self.first_ = None
        self.last_ = None
        self.actual_size_ = 0
        self.max_size_ = max_size

    def is_Empty(self):
        return self.actual_size_ == 0
    
    def is_Full(self):
        return self.actual_size_ == self.max_size_
    
    def __len__(self):
        return self.actual_size_
    
    def insert_begin(self, value_ : int):
        new_node = Node(value_)
        if self.is_Empty():
            print(" Creating the linked list...")
            self.last_ = new_node
        elif self.is_Full():
            raise Exception("Its full...")
        else:
            self.first_.next_.previous_ = new_node
            new_node.next_ = self.first_.next_
        self.first_ = new_node
        self.actual_size_ += 1

    def insert_final(self, value : int):
        new_node = Node(value)
        if self.is_Empty():
            print(" Creating the array ...")
            self.first_ = new_node
        elif self.is_Full():
            raise Exception("Its full...")
        else:
            self.last_.previous_.next_ = new_node
            new_node = self.last_.previous_
        self.last_ = new_node
        self.actual_size_ += 1

    def remove_begin(self):
        if self.is_Empty():
            raise Exception("The list already is empty")
        elif self.actual_size_ == 1:
            self.first_ = None
            self.last_ = None
        else:
            self.first_.next_.previous_ = None
            self.first_ = self.first_.next_
        self.actual_size_ -= 1
            
    def remove_final(self):
        if self.is_Empty():
            raise Exception("The list already is empty")
        elif self.actual_size_ == 1:
            self.first_ = None
            self.last_ = None
        else:
            self.last_.previous_.next_ = None
            self.last_ = self.last_.previous_
        self.actual_size_ -= 1

    def search_begin(self, value : int):
        pointer = self.first_
        while pointer.value_ != value:
            pointer = pointer.next_
            if pointer == self.last_ and self.last_.value_ != value:
                raise Exception("The value is not here")
        return pointer
    
    def search_final(self, value : int):
        pointer = self.last_
        while pointer.value_ != value:
            pointer = pointer.previous_
            if pointer == self.first_ and self.first_.value_ != value :
                raise Exception("The value is not here")
        return pointer
    
    def show_begin(self):
        pointer = self.first_
        while pointer != None:
            print(pointer.value_)
            pointer = pointer.next_

    def show_final(self):
        pointer = self.last_
        while pointer != None:
            print(pointer.value_)
            pointer = pointer.previous_

LL = Linked_List()
LL.insert_begin(1)
LL.search_final(0)