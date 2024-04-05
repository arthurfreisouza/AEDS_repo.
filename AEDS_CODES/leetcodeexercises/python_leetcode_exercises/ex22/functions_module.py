def Media_Function(lst_):
    '''
    O programa calcula a média da lista dada.
    '''
    sum = 0
    for i in lst_:
        sum = sum + i
    media = float(sum / len(lst_))

    return media

def Descrescent_Age_Men(lst_1_, lst_2_, lst_3_):
    '''
    Basicamente, a lista 1 será o nome, a lista 2 a idade e a lista 3 o genêro.
    Criei 3 listas auxiliares da própria função que irão armazenar todos os HOMENS inseridos.
    Após ter as 3 listas de homens, é criado 1 laço for para organizar a lista em ordem Decrescente de idade.
    Irei, ao final de tudo, escrever em 1 arquivo separado todos os resultados.

    '''
    lst_1_mens = []
    lst_2_mens = []
    lst_3_mens = []
    for i in range(len(lst_1_)):
        if str(lst_3_[i].lower()) == 'homem':
            lst_1_mens.append(lst_1_[i])
            lst_2_mens.append(lst_2_[i])
            lst_3_mens.append(lst_3_[i])

    for i in range(len(lst_1_mens)):
        for j in range(i + 1, len(lst_1_mens)):
            if int(lst_2_mens[i]) < int(lst_2_mens[j]):
                aux = lst_2_mens[i]
                lst_2_mens[i] = lst_2_mens[j]
                lst_2_mens[j] = aux

                aux = lst_1_mens[i]
                lst_1_mens[i] = lst_1_mens[j]
                lst_1_mens[j] = aux

                aux = lst_3_mens[i]
                lst_3_mens[i] = lst_3_mens[j]
                lst_3_mens[j] = aux

    for i in range(len(lst_1_mens)):
        with open('/home/arthur/Desktop/my_new_file_2.txt', 'a') as file:
            file.write(str(lst_1_mens[i]))
            file.write(' ')
            file.write(str(lst_2_mens[i]))
            file.write(' ')
            file.write(str(lst_3_mens[i]))
            file.write('\n')



def Girls_Older_Than_20(lst_1_, lst_2_, lst_3_):
    count = 0
    '''
    Irei receber também as mesmas 3 listas igual ao comando acima. 
    Irei criar 1 arquivo que conterá apenas mulheres que tem idade menor do que 20 anos.
    Também terei 1 contador que será incrementado toda vez que encontrar uma mulher com idade menor do que 20 anos.
    '''
    lst_1_womens = []
    lst_2_womens = []
    lst_3_womens = []
    for i in range(len(lst_1_)):
        if str(lst_3_[i].lower()) == 'mulher':
            lst_1_womens.append(lst_1_[i])
            lst_2_womens.append(lst_2_[i])
            lst_3_womens.append(lst_3_[i])

    for i in range(len(lst_1_womens)):

        if int(lst_2_womens[i]) < 20:
            count = count + 1
            with open('/home/arthur/Desktop/my_new_file_3.txt', 'a') as file:
                file.write(str(lst_1_womens[i]))
                file.write(' ')
                file.write(str(lst_2_womens[i]))
                file.write(' ')
                file.write(str(lst_3_womens[i]))
                file.write('\n')
    return count



