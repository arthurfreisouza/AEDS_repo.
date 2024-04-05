import datetime

class Cadastrar:
    
    def __init__(self, name_ : str, age_ : float, date_of_bird_ : datetime):
        self.__name = name_
        self.__age = age_
        self.__date_of_bird = date_of_bird_
        self.__count = 0

    def Register(self):
        if self.Verify():
            self.__count = self.__count + 1
            print(' Your register was finished !')
            self.Write_on_File()
        else:
            print(' You cant make your register, your data is not right.')

    def Verify(self):
        if self.Is_Data_Valid() and self.Older_Than_18():
            return True
        else:
            return False

    def Write_on_File(self):
        with open('/home/arthur/Desktop/blabla.txt', 'a') as file:
            file.write('Name : {}, age : {}, date of bird : {}. \n'.format(self.__name, self.__age, self.__date_of_bird))

    def Is_Data_Valid(self):
        if isinstance(self.__name, str) and isinstance(self.__age, float) and isinstance(self.__date_of_bird, datetime):
            return True
        else:
            return False

    def Older_Than_18(self):
        if self.__age < 18:
            return False
        else:
            return True





