class Funcionario:
    def __init__(self, nome_, cargo_, valor_hora_trabalhada_):
        self.nome = nome_
        self.cargo = cargo_
        self.__valor_hora_trabalhada = valor_hora_trabalhada_
        self.__horas_trabalhadas = 0
        self.__salario = 0
        print('Olá {}, registramos aqui que você é {} e recebe {} reais por hora trabalhada. \n'.format(str(self.nome), str(self.cargo), float(self.__valor_hora_trabalhada)))
 
    def registra_hora_trabalhada(self):
        self.__horas_trabalhadas = float(self.__horas_trabalhadas + 1)
        print('Registrando hora ... \n')
    def calcula_salario(self):
        self.__salario = self.__horas_trabalhadas * self.__valor_hora_trabalhada
        return float(self.__salario)
    

object_1 = Funcionario('Arthur', 'Engenheiro', float(800))

for i in range(10):
    object_1.registra_hora_trabalhada()
    print(i)

print(' Hoje {} recebeu exatamente {} reais. \n'.format(str(object_1.nome), float(object_1.calcula_salario())))