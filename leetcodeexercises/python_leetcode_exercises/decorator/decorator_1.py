def Validar(f, n1_, n2_, n3_):
    if n1_ < 0 or n2_ < 0 or n3_ < 0:
        raise ValueError(' The numbers cant be negative ...')
    else:
        return f(n1_, n2_, n3_)

def Soma(n1_, n2_, n3_):
    return n1_ + n2_ + n3_

while True:
    n1 = int(input(' Write the first number here : '))
    n2 = int(input(' Write the second number here : '))
    n3 = int(input(' Write the third number here : '))   
    final_result = Validar(Soma, n1, n2, n3)
    print(' Sum = {}'.format(final_result))

    play_buttom = str(input(' Press x to exit ...'))
    if play_buttom == 'x':
        break
