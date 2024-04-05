class NPC:
    def __init__(self, name_, intelligence, strength_, resistence_):
        self.name = name_
        self._intelligence = intelligence
        self._strength = strength_
        self._resistence = resistence_
        self.vivo = True

    def info(self):
        print('Nome : {}. '.format(self.name))
        print('Intelligence : {}. '.format(self._intelligence))
        print(' Strength : {}. '.format(self._strength))
        print(' Resistence : {}. '.format(self._resistence))
        print(' Is live : {}. '.format(self.vivo))


class Mage(NPC):
    def __init__(self, name_):
        self._intelligence = 98
        self._strength = 50
        self._resistence = 50
        super().__init__(name_, self._intelligence, self._strength, self._resistence)


class Warrior(NPC):
    def __init__(self, name_):
        self._intelligence = 50
        self._strength = 85
        self._resistence = 80
        super().__init__(name_, self._intelligence, self._strength, self._resistence)


class Druid(NPC):
    def __init__(self, name_):
        self._intelligence = 81
        self._strength = 60
        self._resistence = 78
        super().__init__(name_, self._intelligence, self._strength, self._resistence)

my_mage = Mage('Arthur')
my_warrior = Warrior('Andre')
my_druid = Druid('Matheus')
print('\n')
my_mage.info()
print('\n')
my_warrior.info()
print('\n')
my_druid.info()
my_mage._intelligence = 10000
my_mage.info()