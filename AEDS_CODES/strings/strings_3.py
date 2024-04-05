while True:
    word = str(input())
    if word == "0 0":
        break
    result = ""

    # Separando as words, tenho que transformar individualmente em str.
    value = word.split(" ") # Divide a string em 1 lista com base em 1 identificador.
    value[0] = str(value[0])
    value[1] = str(value[1])


    for char in value[1]: # Para cada letra na word que estamos investigando
        if char == value[0]:
            continue # Irá voltar ao inicio do loop quando encontrar 1 valor que quero tirar.
        else:
            result = result + char # O resultado será os números sem o que eu quero colocar.




    # Se há algum resultado, ou seja, se não eliminamos todos os números temos de retornar 0 ao inves de nulo.
    if result == "":
        result = "0"
    else:
        final_index = None # Index de onde terá o primeiro número diferente de 0.
        if result[0] == "0": # Caso meu resultado final inicie com 0.
            for index,char in enumerate(result):
                if char != "0":
                    final_index = index
                    print(final_index)
                    result = "0" + result[final_index : ]
                    break
                if index == (len(result) - 1) and char == "0":
                    result = "0"
    print(result)

    