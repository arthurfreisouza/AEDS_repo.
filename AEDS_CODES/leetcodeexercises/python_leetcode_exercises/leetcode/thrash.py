# Instanciando a classe.
class MyClass:
    def __init__(self, name_, age_):
        self.name = name_
        self.age = age_

    def __str__(self) -> str:
        return f"KKKK"
    
    def myname(self) -> str:
        print(f"My name is {self.name}")

i1 = MyClass("Arthur", 22)
print(i1.name)
print(i1.age)
print(i1)
i1.myname()

# Alterando atributos da classe
i1.name = "Caio Rococo"
i1.age = 24
print(i1.name)
print(i1.age)
print(i1)

# Apagando atributos da classe
del i1.age
print(i1.age)
print(i1.name)
print(i1)

# Apagando instancia da classe
del i1
print(i1.age)
print(i1.name)
print(i1)