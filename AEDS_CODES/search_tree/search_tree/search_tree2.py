class Node:
    def __init__(self, value):
        self.value_ = value
        self.left_ = None
        self.right_ = None

    def show_value(self):
        print(self.value_)


class BinarySearchTree:
    def __init__(self, max_size : int = 20):
        self.root_ = None
        self.actual_size_ = 0
        self.max_size_ = max_size
    def __len__(self):
        return self.actual_size_

    def is_Empty(self):
        return (self.actual_size_ == 0 or self.root_ == None)

    def is_Full(self):
        return (self.actual_size_ == self.max_size_)
    
    def insert(self, value_ : int):
        new_node = Node(value_)
        if self.is_Empty():
            print(" Creating the binary tree ...")
            self.root_ = new_node
        elif self.is_Full():
            raise Exception("The tree already is fully ...")
        else:
            pointer = self.root_
            while True:
                father = pointer
                if value_ < pointer.value_:
                    pointer = pointer.left_
                    if pointer == None:
                        father.left_ = new_node
                else:
                    pointer = pointer.right_
                    if pointer == None:
                        father.right_ = new_node

    def pre_order(self, node_ : Node):
        if node_ != None:
            print(node_.value_)
            self.pre_order(node_.left_)
            self.pre_order(node_.right_)
            

    def in_order(self, node_ : Node):
        if node_ != None:
            self.in_order(node_.left_)
            print(node_.value_)
            self.in_order(node_.right_)
        

    def pos_order(self, node_ : Node):
        self.pos_order(node_.left_)
        self.pos_order(node_.right_)
        print(node_.value_)

    def search(self, value_) -> Node:
        pointer = self.root_
        while pointer.value_ != value_:
            if value_ < pointer.value_:
                pointer = pointer.left_
            else:
                pointer = pointer.right_
            if pointer == None:
                raise Exception("The value is not here ....")
        return pointer
    


    def remove_val(self, value_):
        pointer = self.root_
        if self.is_Empty():
            raise Exception(" The list already is empty...")
        elif self.actual_size_ == 1:
            self.root_ = None
            self.actual_size_ -= 1
        else:
            while pointer.value_ != value_:
                father = pointer
                is_left_ = None
                if value_ < pointer.value_:
                    pointer = pointer.left_
                    is_left_ = True
                else:
                    pointer = pointer.right_
                    is_left_ = False
                if pointer == None:
                    print("This value is not here...")
                    return
        
        # Agora tenho o pointer no objeto e um no father.
            if pointer.left_ == None and pointer.right_ == None:
                if is_left_ == True:
                    father.left_ = None
                else:
                    father.right_ = None
                self.actual_size_ -= 1
            
            elif pointer.left_ == None and pointer.right_ != None:
                if is_left_ == True:
                    father.left_ = pointer.right_
                else:
                    father.right_ = pointer.right_
                self.actual_size_ -= 1
            
            elif pointer.right_ == None and pointer.left_ != None:
                if is_left_ == True:
                    father.left_ = pointer.left_
                else:
                    father.right_ = pointer.left_
                self.actual_size_ -= 1

            else:
                sucessor = self.get_sucessor(pointer)
                if pointer == self.root_:
                    self.root_ = sucessor
                elif is_left_ == True:
                    father.left_ = sucessor
                else:
                    father.right_ = sucessor
                sucessor.left_ = pointer.left_



    def get_sucessor(self, node : Node):
        pai_sucessor = node
        sucessor = node
        actual_pointer = node.right_
        while actual_pointer != None:
            pai_sucessor = sucessor
            sucessor = actual_pointer
            actual_pointer = actual_pointer.left_
        
        if sucessor != node.right_:
            pai_sucessor.left_ = sucessor.right_
            sucessor.right_ = node.right_
        return sucessor
                
