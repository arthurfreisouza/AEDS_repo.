# Fazendo as condições do exercicio e as testando.
import sys
number_ = int(input())
cond1 = 2 <= number_ <= 10000
cond2 = (number_ % 2 == 0)
if not(cond1) or not(cond2):
    sys.exit()

# Separando as strings de entrada em 1 array da numeração e o pé.
feets = []
for i in range(number_):
    word = str(input())
    feets.append(word.split(" "))

# Criando 1 lista com todas as combinações dos pés que poderão ter.
str1 = "D"
str2 = "E"
lst_of_v = []
for i in range(30, 61):
    lst_of_v.append([str(i), str1])
    lst_of_v.append([str(i), str2])

# Irei pegar os pares de pés e contar quantos pares terão(valor minimo).
count = 0
for index in range(0, len(lst_of_v), 2):
    if index == 59:
        break
    count_feet_1 = feets.count(lst_of_v[index])
    count_feet_2 = feets.count(lst_of_v[index + 1])
    if count_feet_1 != 0:
        count = count + min(count_feet_1, count_feet_2)
print(count)
