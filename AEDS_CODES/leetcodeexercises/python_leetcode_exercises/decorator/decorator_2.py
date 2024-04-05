def Validar(f):
    def valida(x,y):
        if x < 0 or y < 0:
            raise ValueError(' We cant insert negative numbers ...')
        return f(x,y)
    return valida
    
@Validar
def Soma(n1, n2):
    return n1 + n2

returned_value = Soma(10, -20)
print(returned_value)