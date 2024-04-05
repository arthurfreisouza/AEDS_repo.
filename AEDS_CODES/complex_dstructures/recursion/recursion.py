#def recursion(i):
#        print(f"Arthur, {i}")
#    i += 1
#    if i == 5:
#        return
#    else:
#        recursion(i)
#
#recursion(0)

#def factorial(n):
#    if n == 0 or n == 1:
#        return 1
#    
#    else:
#        return n * factorial(n -1)
#    
#
#def fibbonnaci(n):
#    if n == 0:
#        return 0
#    elif n == 1:
#        return 1
#    else:
#        return fibbonnaci(n - 1) + fibbonnaci(n - 2)
    





#def soma(n, result = 0):
#    print(f"result = {result}, n = {n}")
#    result += n
#    if n == 0:
#        return 0
#    return soma(n = n -1, result = result)

#def soma(n):
#    if n == 0:
#        return 0
#    else:
#        return n + soma(n -1)
#
#print(soma(5))

#def even_numbers(num):
#    print(num)
#    if num <= 2:
#        return num
#    else:
#        return even_numbers(num - 2)
#
#even_numbers(8)

#def fibonnaci(idx):
#    if idx <= 1:
#        return idx
#    else:
#        return fibonnaci(idx - 1) + fibonnaci(idx -2)
#    
#print(fibonnaci(8))

#try:
#    def factorial(num : int):
#
#        print(num)
#        if num <= 1:
#            return 1
#        else:
#            return (num * factorial(num - 1))
#    print(factorial("a"))
#    
#
#except:
#    print(" The value is not an integer, type other value ... ")


#def calcula_exponencial(valor, exp):
#    print(valor)
#    if exp == 0:
#        return 1
#    else:
#        return valor * calcula_exponencial(valor, exp - 1)
#    
#calcula_exponencial(5, 4)

#import sys
#def show_numbers(value : int):
#    print(value)
#    if value == 0:
#        return
#    return show_numbers(value - 1)
    

    
#result = ""
#def reverse_string(my_str : str, result_ = result):
#
#    result_ = str(result_ + my_str[len(my_str) - 1])
#    if len(my_str) == 1:
#        result_ = str(result_ + my_str)
#        my_str = ""
#    if len(my_str) == 0:
#        return result_
#    else:
#        return reverse_string(my_str[:len(my_str) - 1])



#import math
#def is_prime(number : int, idx : int = 0):
#    idx_max = pow(number, 0.5)
#    if idx == idx_max:
#        return False
#    elif number == 1:
#        return True
#    else:
#        return (number // idx == 0 and is_prime(number, idx + 1))
#    



#def is_prime(number : int, idx : int = 2):
#
#    if idx == number:
#        return True
#    else:
#        return (number % idx != 0 and is_prime(number, idx + 1))
#    
#
#print(is_prime(14))



def power(number : int):
    if number <= 0 :
        return False
    elif number == 1:
        return True
    else:
        return (number % 3 == 0 and power(number // 3))