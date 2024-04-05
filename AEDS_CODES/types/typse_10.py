def reduce(x : int) -> int:
    return x - 1

word_lst = str(input()).split(" ")
n_pos = int(word_lst[0])
seq = int(word_lst[1])


cond1 = (2 <= n_pos <= 100000)
cond2 = (2 <= seq <= 100000)

lst_numbers = str(input()).split(" ")
lst_index = str(input()).split(" ")
lst_index = list(map(int, lst_index))
lst_index = list(map(reduce, lst_index))

if cond1 == True and cond2 == True:
    for i in lst_index:
        lst = lst_numbers[0 : i] #PEGA TODOS OS NUMEROS?
        for i in lst:
            pass