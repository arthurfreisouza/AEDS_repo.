import datetime
class Bank:
    def __init__(self, name_ : str, email_: str, cpf_: int, profission_:str, date_of_birth_ : str, salary_ : float):
        self.__name = name_
        self.__email = email_
        self.__cpf = cpf_
        self.__profission = profission_
        self.__date_of_birth = date_of_birth_
        self.Convert_Data()
        self.__salary = salary_

    def Register(self) -> bool:
        if self.Valid():
            print(' Registering ...')
            self.Write_On_File()
        else:
            print('Are there some invalid data ...')
            self.Write_On_File_Wrong()

    def Valid(self) -> bool:
        if self.Age_Valid() and self.Salary_Valid():
            return True
        else:
            return False

    def Age(self) -> float:
        today = datetime.datetime.now()
        difference = today - self.__date_of_birth
        difference = difference.days
        age =  difference / 365.25
        return age
    
    def Age_Valid(self) -> bool:
       if self.Age() < 18:  
           return False
       else:
           return True
       
    def Salary_Valid(self):
       if self.__salary < 10000:
           return False
       else:
           return True
       
    def Get_Bank(self):
        return str('/home/arthur/Desktop/{}'.format(self.__class__.__name__))
    
    def Write_On_File(self):
        with open('{}.txt'.format(self.Get_Bank()), 'a') as file:
            file.write(' User {}, with CPF {} now is registered {}. \n'.format(self.__name, self.__cpf, datetime.datetime.now()))

    def Write_On_File_Wrong(self):
        with open('{}_wrong.txt'.format(self.Get_Bank()), 'a') as file:
            file.write(' User {}, with CPF {} is not registered {}. \n'.format(self.__name, self.__cpf, datetime.datetime.now()))
    
    def Convert_Data(self):
        self.__date_of_birth  = datetime.datetime.strptime(self.__date_of_birth,'%d/%m/%Y')
        self.__date_of_birth  = datetime.datetime.strftime(self.__date_of_birth,'%d/%m/%Y')
        self.__date_of_birth  = datetime.datetime.strptime(self.__date_of_birth,'%d/%m/%Y')
        self.__date_of_birth = datetime.datetime.strftime(self.__date_of_birth, '%Y/%m/%d')
        self.__date_of_birth  = datetime.datetime.strptime(self.__date_of_birth,'%Y/%m/%d')