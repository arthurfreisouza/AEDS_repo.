class NPC:
    def __init__(self, name_, age_, qi_):
        self.name = name_
        self.age = age_
        self.qi = qi_
        self.__test = 'Criado do lado de dentro da classe.'
    
    def getTest(self):
        return self.__test
    
    def setTest(self, new_test):
        self.__test = new_test
        return self.__test

object_1 = NPC('Behhemoth', 22, 178)

object_1.__test = 'Criado do lado de fora da classe.'
print(object_1.__test)
value = object_1.getTest()
print(value)
object_1.setTest(' Valor alterado...')
value = object_1.getTest()
print(value)
