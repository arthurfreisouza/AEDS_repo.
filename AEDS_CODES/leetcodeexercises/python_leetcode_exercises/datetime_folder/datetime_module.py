from datetime import datetime, timedelta


date_now = datetime.now()
tomorrow = date_now + timedelta(days = 1)
print(date_now.date())
print(tomorrow.date())
digit_year = int(input(' Write a year : '))
digit_month = int(input(' Write a month : '))
digit_day = int(input(' Write a day : '))
new_date = datetime(digit_year, digit_month, digit_day)
print(new_date)
print(new_date.date())
delay = (date_now - new_date).days / 365.25
print(delay)

contract_data = '07/01/2000'
print(contract_data)
contract_data = datetime.strptime(contract_data, '%d/%m/%Y')
print(contract_data)

contract_data = datetime.strftime(contract_data,'%d/%m/%Y')
print(contract_data)