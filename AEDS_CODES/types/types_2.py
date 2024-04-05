import sys
# Pegando todos os valores e criando as condicionais os tenstando...
num_sq = int(input())
str_values = str(input())
lst_of_values = str_values.split(" ")
condition = 3 < num_sq < 10000
# Caso tenha algum valor incorreto, lance uma exceção...
#if "0" not in lst_of_values or num_sq != len(lst_of_values) or condition == False:
#   raise Exception(f"TA ERRADO.")

new_lst = []
for index, value in enumerate(lst_of_values):
    v1 = 10000
    v2 = 10000
    count = 0
    if value == "-1":
        for i in range(index, -1, -1): #index 0 nao ta pegando o 0  para a entrada 0 -1 -1 -1 -1 -1
            if lst_of_values[i] == "0":
                v1 = count
                break
            else:
                count = count + 1
        count = 0

        for i in range(index, len(lst_of_values)):
            if lst_of_values[i] == "0":
                v2 = count
                break
            else:
                count = count + 1

        if int(v2) < int(v1):
            new_lst.append(v2)
        else:
            new_lst.append(v1)
    else:
        new_lst.append(0)


new_lst = [str(value) for value in new_lst]
str_result = " ".join(new_lst)
print(str_result)