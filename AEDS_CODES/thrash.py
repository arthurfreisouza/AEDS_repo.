arr = []
arr = str(input()).split(" ")
arr = list(map(int, arr))

def movezeros(arr_ : list[int]) -> None:
    prev_index = 0 # Essa variável irá armazenar o valor do índice que terá o 0.
    for i in range(0, len(arr_)):
        if arr_[i] != 0:
            hold = arr_[prev_index] # Guardando o 0.
            arr_[prev_index] = arr_[i] # Onde tinha o 0 agora tem um número não nulo.
            arr_[i] = hold # Onde tinha o número não nulo agora tem o 0.
            prev_index += 1
    print(arr_)

movezeros(arr)