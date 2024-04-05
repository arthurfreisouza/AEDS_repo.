import sys

def validacao_divisao(func):
    def validacao(x, y):
        if y != 0:
            return func(x, y)
        else:
            print('Erro: Divisão por zero.')
            sys.exit()
    return validacao

@validacao_divisao
def dividir(x, y):
    return x / y

# Exemplo de uso
num1 = float(input("Digite o numerador: "))
num2 = float(input("Digite o denominador: "))

resultado = dividir(num1, num2)
print(f"Resultado da divisão: {resultado}")
