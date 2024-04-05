'''# Complexidade espacial = 2 * 
def inverter_list(lista):
    tamanho = len(lista) # 1
    limite = tamanho // 2 # 2
    tamanho = tamanho -1
    for i in range(limite): # 3
        aux = lista[i] # 3
        lista[i] = lista[tamanho - i] # 4
        lista[tamanho - i] = aux
    print(lista)

inverter_list([1, 2, 3, 4, 5, 6])'''


def busca(lista, valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i
    return None
    
lista_estranha = [8, "5", 32, 0, "python", 11]
elemento = 32

indice = busca(lista_estranha, elemento)
if indice is not None:
    print(f"The indice is {indice}")
else:
    print("FDASA")