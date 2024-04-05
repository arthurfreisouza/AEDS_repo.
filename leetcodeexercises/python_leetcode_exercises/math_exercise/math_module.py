import matplotlib.pyplot as plt
import numpy as np
import sys

args = sys.argv

class Operation:
    def __init__(self, op_name_ : str):
        self.__op_name = op_name_
        self.__x = np.arange(0, 100, 10)
        self.Which_Operation()
    
    def Which_Operation(self):
        if self.__op_name.lower() == 'linear':
            linear_function = self.Linear_Function(self.__x)
            plt.figure(1)
            plt.plot(self.__x, linear_function)
            plt.suptitle(' General title ! ')
            plt.show()
        elif self.__op_name.lower() == 'exponential':
            exp_ = self.Exponential_Function(self.__x)
            plt.figure(1)
            plt.plot(self.__x, exp_)
            plt.suptitle(' General title ! ')
            plt.show()
        elif self.__op_name.lower() == 'logaritmic':
            log_ = self.Logaritmic_Function(self.__x)
            plt.figure(1)
            plt.plot(self.__x, log_)
            plt.suptitle(' General title ! ')
            plt.show()
        elif self.__op_name.lower() == 'sec_degree':
            sec_degree_function = self.Second_Degree_Function(self.__x)
            plt.figure(1)
            plt.plot(self.__x, sec_degree_function)
            plt.suptitle(' General title ! ')
            plt.show()

        elif self.__op_name.lower() == 'senoidal':
            cos_, sin_, tan_ = self.Senoidal_Function(self.__x)
            #fig1, ax = plt.subplots(nrows = 2, ncols = 2)
            #ax[0,0].plot(self.__x, cos_)
            #ax[0,1].plot(self.__x, sin_)
            #ax[1,0].plot(self.__x, tan_)
            fig1 = plt.figure(1)
            #ax1 = fig1.add_subplot(2, 2, 1)
            #ax2 = fig1.add_subplot(2, 2, 2)
            ax3 = fig1.add_subplot(2, 2, 3)
            #ax1.plot(self.__x, cos_)
            #ax2.plot(self.__x, sin_)
            ax3.plot(self.__x, tan_)
            #ax1.set_title('Subplot 1')
            #ax2.set_title('Subplot 2')
            ax3.set_title('Subplot 3')
            plt.tight_layout()
            fig1.suptitle(' General title ! ')
            plt.show()
        else:
            raise Exception(' Does not exists this type of operation ...')
        
    def Linear_Function(self, x):
        return float(x + 1)
    def Exponential_Function(self, x):
        return float(np.exp(x))
    def Logaritmic_Function(self, x):
        return float(np.log(x))
    def Second_Degree_Function(self, x):
        return float(x ** 2)
    def Senoidal_Function(self, x):
        return (np.tan(x))
    

object = Operation(args[1])
    
