word = str(input("Write yout word."))

my_lst = []
len_word = len(word)
vogals = ('a','e','i','o','u')

# Varrendo toda a string e armazenando as vogais.
if word == word.lower() and len(my_lst) <= 50:
    for i in word:
        if i in vogals:
            my_lst.append(i)

# Comparando os elementos da lista.
var = 1
for i in range(len(my_lst) // 2):
    if my_lst[i] != my_lst[len(my_lst) - 1 - i ]:
        var = 0
        break
if var == 0 or len(my_lst) == 0:
    print("N")
else:
    print("S")
