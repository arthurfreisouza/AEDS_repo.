from class_bank import Bank
import sys


lst = []
while True:
    play_button = str(input(' Press s to insert or x to exit...'))
    if play_button == 's':
        name = str(input( 'Write your name here : '))
        email = str(input( 'Write your email here : '))
        cpf = int(input( 'Write your cpf here : '))
        prof = str(input( 'Write your prof here : '))
        date_of = str(input( 'Write your date here : '))
        salary = float(input( 'Write your salary here : '))
        value = Bank(name, email, cpf, prof, date_of, salary)
        value.Register()
        lst.append(value)
    elif play_button == 'x':
        print(' Getting out...')
        break
    else:
        print('Press the button again ...')

        
#if len(args) != 7:
#    sys.exit()

print(' Finishing the program ... ')

with open('/home/arthur/Desktop/Bank.txt', 'r') as file:
    aux = file.read()

print(aux)
print(10 * '\n')

with open('/home/arthur/Desktop/Bank_wrong.txt', 'r') as file:
    aux = file.read()

print(aux)