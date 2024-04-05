#class my_class:
#    def __init__(self, *args : int):
#        self.my_list_ = []
#        for i in args:
#            self.my_list_.append(i)
#    
#    def __str__(self):
#        return f"OK"
#    def len(self):
#        return len(self.my_list_)
#    
#    def get_sum(self) -> float:
#        result = (self.my_list_[0] + self.my_list_[len(self.my_list_) - 1]) * len(self.my_list_) / 2
#        return result

#list1 = ['A', 'B', 'C']
#list2 = [1, 2, 3]
#
#for my_var in zip(list1, list2):
#    print(my_var)


class aluno:
    def __init__(self, name_ : str, v1_ : float, v2_ : float):
        self.name = name_
        self.v1 = v1_
        self.v2 = v2_

    def average(self) -> float:
        result = (self.v1 + self.v2) / 2
        return result

    def show_data(self):
        print(self.name)
        print(self.v1)
        print(self.v2)

    def result(self):
        aux = self.average()
        cond = aux >= 6
        if cond == True:
            print("Aprovado.")
        else:
            print("Reprovado.")
