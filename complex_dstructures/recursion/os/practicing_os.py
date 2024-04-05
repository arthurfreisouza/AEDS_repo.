import os

arquivos_extraidos = []

def pegar_arquivos_pasta(pasta : str):
    lista_arquivos = os.listdir(pasta)
    for arquivo in lista_arquivos:
        if ".txt" in arquivo and "Vendas" in arquivo:
            nome_mes = arquivo.split()[-1].replace(".txt", "")
            arquivos_extraidos.append(nome_mes)
        elif ".txt" not in arquivo:
            pegar_arquivos_pasta(f"{pasta}/{arquivo}")

pegar_arquivos_pasta("Arquivos")
print(arquivos_extraidos)