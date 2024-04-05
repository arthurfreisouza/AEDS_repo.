import sys
word1 = str(input())
word2 = str(input())
lst = []
lst2 = []
if len(word1) != len(word2):
    print("N")
    sys.exit()

# Pegando todas as letras dentro de cada string.
for index, char in enumerate(word1):
    lst.append(word1[index])
    lst2.append(word2[index])

# Os tamanhos tem de ser iguais.
if len(lst) != len(lst2):
    print("N")
    sys.exit()
else:
    # Irei varrer os valores da lista2, e remover de ambas as listas as letras iguais.
    for index, char in reversed(list(enumerate(lst2))):
        if char != "*" and char in lst:
           lst.remove(char)
           lst2.remove(char)


# O tamanho tem de ser igual para ambas as listas agora.
if len(lst) != len(lst2):
    print("N")
    sys.exit()
else:
    if len(lst) != 0:
        for char in lst2:
            if char != "*":
                print("N")
                sys.exit()
    print("S")