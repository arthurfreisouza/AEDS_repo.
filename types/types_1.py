import sys

def main():
    try:
        # Usando o Try Exception para monitorar os tipos das variáveis.
        len_arr = int(input())   
        str_of_v = str(input())
        lst_of_v = str_of_v.split(" ") # Criando 1 lista de valores com a divisao de espaço.
    except Exception as error:
        print(f"The error {error} is happening.. \n")
        sys.exit()

    # Gerando 1 erro caso os tamanhos sejam diferentes.
    if len(lst_of_v) != len_arr:
         sys.exit()

    result_lst = []
    index = 0
    while index < len(lst_of_v): # Percorrendo toda a lista...
        count = 0
        # Seguindo a lista de valores na memória...
        for index2 in range(index, len(lst_of_v)):
            if lst_of_v[index] == lst_of_v[index2]: # Verificando se são iguais...
                count += 1
            else:
                break

        # Colocando os valores em 1 lista 
        result_lst.append(count)
        index = index + count

    # Voltando o valor máximo...
    print(max(result_lst))

if __name__ == "__main__":
    main()


























