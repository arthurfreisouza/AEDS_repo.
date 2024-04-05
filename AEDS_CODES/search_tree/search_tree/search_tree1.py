
ROOT = "root"
class Node: # Criando a classe árvore binária.
    def __init__(self, value_ : int):
        self.value_ = value_
        self.left_ = None
        self.right_ = None
    def show_actual_val(self):
        print(self.value_)



class Binary_Search_Tree:
    def __init__(self):
        self.root_ = None
        self.actual_size = 0
        self.graphviz = []

    def isEmpty(self):
        return (self.root_ == None)

    def __len__(self):
        return self.actual_size

    def insert(self, val_ : int):
        new_node = Node(val_)
        if self.isEmpty():
            print(" Creating the tree...")
            self.root_ = new_node
        else:
            pointer = self.root_
            while True:
                father = pointer
                if val_ < pointer.value_:
                    pointer = pointer.left_
                    if pointer == None:
                        father.left_ = new_node
                        self.graphviz.append(str(father.value_) + "->" + str(new_node.value_))
                        self.actual_size += 1
                        return
                else:
                    pointer = pointer.right_
                    if pointer == None:
                        father.right_ = new_node
                        self.graphviz.append(str(father.value_) + "->" + str(new_node.value_))
                        self.actual_size += 1
                        return
                    
    def search(self, val_ : int):
        pointer = self.root_
        while pointer.value_ != val_:
            if pointer.value_ < val_:
                pointer = pointer.right_
            else:
                pointer = pointer.right_
            if pointer == None and self.root_ != None:
                raise Exception("The value is not here ...")
        return pointer
    
    def show_pre_order(self, node : Node):
        if node != None:
            print(node.value_)
            self.show_pre_order(node.left_)
            self.show_pre_order(node.right_)

    def show_in_order(self, node : Node):
        if node != None:
            self.show_in_order(node.left_)
            print(node.value_)
            self.show_in_order(node.right_)

    def show_pos_order(self, node : Node):
        if node != None:
            self.show_pos_order(node.left_)
            self.show_pos_order(node.right_)
            print(node.value_)
    def min(self, node = None):
        if node == None:
            node = self.root_
        while node.left_:
            node = node.left_
        return node.value_
    def max(self, node = None):
        if node == None:
            node = self.root_
        while node.right_:
            node = node.right_
        return node            
#
#    def remove(self, val_ : int):
#        if self.isEmpty():
#            raise Exception("The list is empty...")
#        else:
#            actual_pointer = self.root_
#            father = self.root_
#            elem_is_left = None
#
#            while True:
#                father = actual_pointer # O ponteiro father irá sempre apontar para o nó anterior ao atual.
#                if actual_pointer.value_ == val_:
#                    break
#                elif val_ < actual_pointer.value_:
#                    actual_pointer = actual_pointer.left_
#                    elem_is_left = True
#                else:
#                    actual_pointer = actual_pointer.right_
#                    elem_is_left = False
#                
#                if actual_pointer == None:
#                    return False
#            # Agora, o ponteiro actual_pointer terá o nó que será apagado, o father terá o elemento anterior.
#                
#            if actual_pointer.left_ == None and actual_pointer.right_ == None: # Não tem filhos.
#                if actual_pointer == self.root_:
#                    self.root_ = None
#                elif elem_is_left == True:
#                    father.left_ = None
#                    self.graphviz.remove(str(father.value_) + "->" + str(actual_pointer.value_))
#                else:
#                    father.right_ = None
#                    self.graphviz.remove(str(father.value_) + "->" + str(actual_pointer.value_))
#
#            elif actual_pointer.left_ == None and actual_pointer.right_ != None:
#                if elem_is_left == False:
#                    father.right_ = actual_pointer.right_
#                else:
#                    father.left_ = actual_pointer.right_
#            elif actual_pointer.left_ != None and actual_pointer.right_ == None:
#                if elem_is_left == False:
#                    father.right_ = actual_pointer.left_
#                else:
#                    father.right_ = actual_pointer.left_
#
#            else: # Caso tenha 2 filhos, irei substituí-lo pelo seu sucessor em ordem.
#                sucessor = self.get_sucessor(actual_pointer)
#                if actual_pointer == self.root_:
#                    self.root_ = sucessor
#                elif elem_is_left == True:
#                    father.left_ = sucessor
#                else:
#                    father.right_ = sucessor
#                sucessor.left_ = actual_pointer.left_
#
#
#    def get_sucessor(self, node : Node):
#        pai_sucessor = node
#        sucessor = node
#        actual_pointer = node.right_
#        while actual_pointer != None:
#            pai_sucessor = sucessor
#            sucessor = actual_pointer
#            actual_pointer = actual_pointer.left_
#        if sucessor != node.right_:
#            pai_sucessor.left_ = sucessor.right_
#            sucessor.right_ = node.right_
#        return sucessor


    def remove2(self, value_ , node = ROOT):
        if node == ROOT:
            node = self.root_

        if node == None:
            return node

        if value_ < node.value_:
            node.left_ = self.remove2(value_, node.left_)
        elif value_ > node.value_:
            node.right_ = self.remove2(value_, node.right_)
        else: # Quando chega ao valor desejado.
            if node.left_ == None:
                return node.right_
            elif node.right_ == None:
                return node.left_ 
            else:
                susbtitute = self.min(node.right_)
                node.value_ = susbtitute
                node.right_ = self.remove2(susbtitute, node.right_)
        return node
                
