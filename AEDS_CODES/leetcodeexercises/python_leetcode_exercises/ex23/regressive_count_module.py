import time

def Validar(f):
    def valida( number_, time_speed_):
        if number_ < 0 or time_speed_ < 0:
            raise ValueError(' These values need to be grand than 0.')
        return f(number_, time_speed_)
    return valida





@Validar
def Regressive_Count_Function(number_, time_speed_):
    for i in range(number_, 0, -1):
        print('{}'.format(int(i)))
        time.sleep(time_speed_)