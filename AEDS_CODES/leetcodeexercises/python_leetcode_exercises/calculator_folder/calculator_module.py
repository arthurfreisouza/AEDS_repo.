import sys
from datetime import datetime
class Calculator:
    def __init__(self, op_ : str, n1_ : float, n2_ : float):
        self.__op = op_
        self.__n1 = n1_
        self.__n2 = n2_
        self.__Calculator_Function()

    def __Calculator_Function(self):
        result = self.__Wich_Op()
        my_timer = datetime.now()
        print(' The result of {} between {} and {} is {}. \n'.format(self.__op, self.__n1, self.__n2, result))
        with open('/home/arthur/Desktop/Calculator_file.txt', 'a') as file:
            file.write(' The result of {} between {} and {} is {}. The time when thiis operation occur : {}\n'.format(self.__op, self.__n1, self.__n2, result, my_timer))

    def __Wich_Op(self):
        if self.__op.lower() == 'sum':
            return self.__Sum()   
        elif self.__op.lower() == 'sub':
            return self.__Sub()
        elif self.__op.lower() == 'mult':
            return self.__Mult()
        elif self.__op.lower() == 'div':
            if self.__n2 == 0:
                raise Exception(' Its a division by zero. ')
            return self.__Div()
        elif self.__op.lower() == 'pot':
            return self.__Pot()
        else:
            print('We have not this operation ...')
            sys.exit()
        
    def __Div(self):
        return float(self.__n1 / self.__n2)
                
    def __Sum(self):
        return (self.__n1 + self.__n2)
    
    def __Sub(self):
        return (self.__n1 - self.__n2)
    
    def __Mult(self):
        return (self.__n1 * self.__n2)
    
    def __Pot(self):
        return (self.__n1 ** self.__n2)