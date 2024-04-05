import sys

# Lendo os valores da lista de valores fixos.
number1 = int(input())
my_set = set()
for i in range(number1):
    value = int(input())
    my_set.add(value)
cond1 = 1 <= number1 <= 50

# Lendo os valores da lista de valores de teste.2 
number2 = int(input())
cond2 = 1 <= number2 <= 10000

# Satisfazendo as condições
if cond1 == False or cond2 == False:
    sys.exit()

#my_set_test = set()
#for i in range(number):
#    if my_set_test[i] in my_set:
#        print("Sim")
#    else:
#        print("Nao")
    
for i in range(number2):
    value = int(input())
    if value in my_set:
        print("Sim")
    else:
        print("Nao")

