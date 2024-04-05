import datetime

class Person:
    '''
    This class wiil...
    '''
    def __init__(self, name_ : str, country_ : str, date_of_bird_ : str):
        self.day = 0
        self.month = 0
        self.year = 0
        self.name = name_
        self.country = country_
        self.is_live = True
        for i in range(31):
            if(date_of_bird_[0:2] == str(i)):
                self.day = int(i)
        for i in range(12):
            if(date_of_bird_[3:5] == str(i)):
                self.month = int(i)
        for i in range(3000):
            if(date_of_bird_[-4:] == str(i)):
                self.year = int(i)
        self.your_date = datetime.datetime(self.year, self.month, self.day)

    def getName(self) -> str:
        return self.name
    
    def getCountry(self) -> str:
        return self.country
    
    def getAge(self) -> int:
        actual_data = datetime.now()
        diferenca = actual_data - self.your_date
        age = float(diferenca.days / 365)
        return age
    
    def getDate_Of_Bird(self) -> datetime:
        return self.your_date
















from datetime import datetime

class Person:
    '''
    This class will...
    '''
    def __init__(self, name_: str, country_: str, date_of_birth_: str):
        self.day = 0
        self.month = 0
        self.year = 0
        self.name = name_
        self.country = country_
        self.is_live = True

        # Separar a entrada da data nas partes (dia, mês, ano)
        day, month, year = map(int, date_of_birth_.split('/'))

        if 1 <= day <= 31:
            self.day = day

        if 1 <= month <= 12:
            self.month = month

        if 1 <= year <= 3000:
            self.year = year

        self.your_date = datetime(self.year, self.month, self.day)

    def getName(self) -> str:
        return self.name
    
    def getCountry(self) -> str:
        return self.country
    
    def getAge(self) -> float:
        actual_data = datetime.now()
        difference = actual_data - self.your_date
        age = float(difference.days / 365.25)  # Considerando anos bissextos
        return age
    
    def getDateOfBirth(self) -> datetime:
        return self.your_date
