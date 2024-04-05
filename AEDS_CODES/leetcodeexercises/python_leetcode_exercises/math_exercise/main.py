import matplotlib.pyplot as plt
import numpy as np
import sys

args = sys.argv
t = np.linspace(1, 10, 100)


def Validate(function_):
    def validate(t_):
        if np.any(t_ < 0.9):
            raise Exception('Incorrect value. Some values are not greater than 0.9.')
        else:
            return function_(t_)
    return validate

@Validate
def Log_Function(t_):
    '''
    A função logaritmica irá aceitar valores iniciais começando a partir de 1.
    '''
    return np.log10(t_)

def Exp_Function(t_):
    return np.exp(t_)

def Second_Degree_Function(t_):
    return t_ ** 2

def Linear_Function(t_):
    return t_ + 1

def Which_Operation(op_ : str):
    if op_.lower() == 'log':
        y = Log_Function(t)
        fig1 = plt.figure('1')
        fig1.clf()
        fig1.suptitle(' Logaritmic graph')
        ax = fig1.add_subplot()
        ax.plot(t, y)
        ax.set_xlabel('t')
        ax.set_ylabel('log')
        plt.show()
    elif op_.lower() == 'exp':
        y = Exp_Function(t)
        fig1 = plt.figure('1')
        fig1.clf()
        fig1.suptitle(' Exponential graph')
        ax = fig1.add_subplot()
        ax.plot(t, y)
        ax.set_xlabel('t')
        ax.set_ylabel('exp')
        plt.show()
    elif op_.lower() == 'second_degree':
        y = Second_Degree_Function(t)
        fig1 = plt.figure('1')
        fig1.clf()
        fig1.suptitle(' Second degree graph')
        ax = fig1.add_subplot()
        ax.plot(t, y)
        ax.set_xlabel('t')
        ax.set_ylabel('sec')
        plt.show()
    elif op_.lower() == 'linear':
        y = Linear_Function(t)
        fig1 = plt.figure('1')
        fig1.clf()
        fig1.suptitle(' Linear graph')
        ax = fig1.add_subplot()
        ax.plot(t, y)
        ax.set_xlabel('t')
        ax.set_ylabel('linear')
        plt.show()

Which_Operation(args[1])
