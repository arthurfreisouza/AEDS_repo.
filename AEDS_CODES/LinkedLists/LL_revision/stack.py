class Node:
    def __init__(self, names):
        self.name_ = names
        self.next_ = None
    def show_val(self):
        print(self.name_)


class Stack:
    def __init__(self, max_size : int = 5):
        self.head_ = None
        self.max_size_ = max_size
        self.actual_size_ = 0

    def __len__(self):
        return self.actual_size_

    def is_Empty(self):
        return (self.actual_size_ == 0)

    def is_Full(self):
        return (self.actual_size_ == self.max_size_)
    
    def append_stack(self, name):
        new_node = Node(name)
        if self.is_Empty():
            print(" Creating the list ... ")
            self.head_ = new_node
        elif self.is_Full():
            raise Exception("It's already is full...")
        else:
            pointer = self.head_
            while pointer.next_ != None:
                pointer = pointer.next_

            pointer.next_ = new_node
        self.actual_size_ += 1

    def remove_stack(self):
        pointer = self.head_

        while pointer.next_.next_ != None:
            pointer = pointer.next_
        
        pointer.next_ = None
        self.actual_size_ -= 1


    def show_all_array(self):
        if self.is_Empty():
            print("It's empty !")
            return
        else:
            pointer = self.head_
            while pointer != None:
                pointer.show_val()
                pointer = pointer.next_
























































class Queue:
    def __init__(self, max_size : int = 10):
        self.head_ = None
        self.max_size_ = max_size
        self.actual_size_ = 0

    def __len__(self):
        return self.actual_size_

    def is_Empty(self):
        return self.actual_size_ == 0

    def is_Full(self):
        return self.actual_size_ == self.max_size_
    
    def insert_in_queue(self, value : str):
        new_node = Node(value)
        if self.is_Empty():
            self.head_ = new_node
            print("Creating the queue...")
        elif self.is_Full():
            raise Exception("It's already full...")
        else:
            pointer = self.head_
            while pointer.next_ != None:
                pointer = pointer.next_
            pointer.next_ = new_node
            print("Inserted")
        self.actual_size_ += 1

    
    def delete_in_queue(self):
        if self.is_Empty():
            raise Exception(" Its empty...")
        else:
            temp = self.head_.name_
            self.head_ = self.head_.next_
        self.actual_size_ -= 1
        return temp


    def show_all_array(self):
        pointer = self.head_

        while pointer != None:
            pointer.show_val()
            pointer = pointer.next_
        print("'-'")