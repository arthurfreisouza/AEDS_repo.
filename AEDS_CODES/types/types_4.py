def main():
    inp1 = str(input())
    lst_ = inp1.split(" ")
    len_album = int(lst_[0])
    special_fig = int(lst_[1])
    len_my_figs = int(lst_[2])
    del lst_

    inp1 = str(input())
    special_figs = inp1.split(" ")
    cond4 = 1 <= len(special_figs) <= len_album


    inp1 = str(input())
    my_figs = inp1.split(" ")

    # Transformando tudo em inteiro, e usamos a função set para eliminar os valores repetidos.
    # Tambem poderia usar a função map => map(int, array).
    special_figs = [int(numero) for numero in special_figs]
    my_figs = [int(numeros) for numeros in my_figs]
    set_special_figs = set(special_figs)
    set_my_figs = set(my_figs)

    # Pegando o tamanho da diferença entre os arrays.
    diff = (len(set_special_figs.difference(set_my_figs)))
    print(diff)

if __name__ == "__main__":
    main()
