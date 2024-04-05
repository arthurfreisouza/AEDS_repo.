class Funcionario:
    def __init__(self, name_, salario_base_):
        self.name = name_
        self.salario_base = salario_base_
    def Calcular_Salario():
        pass

class Analista(Funcionario):
    def Calcular_Salario(self):
        return self.salario_base * 1.1
    
class Gerente(Funcionario):
    def __init__(self, nome_, salario_base_, bonus_):
        super().__init__(nome_, salario_base_)
        self.bonus = bonus_
    def Calcular_Salario(self):
        return self.salario_base + self.bonus
    
class Estagiario(Funcionario):
    def Calcular_Salario(self):
        return self.salario_base
    

def Exibir_Salario(func_name_):
    return func_name_.Calcular_Salario()


analyst = Analista(' Matheus', 8000)

gerent = Gerente(' Marcio', 12000, 2000)

trainee = Estagiario('Arthur', 2000)

print(' Salário de {} : {}'.format(analyst.name, Exibir_Salario(analyst)))
print(' Salário de {} : {}'.format(gerent.name, Exibir_Salario(gerent)))
print(' Salário de {} : {}'.format(trainee.name, Exibir_Salario(trainee)))

