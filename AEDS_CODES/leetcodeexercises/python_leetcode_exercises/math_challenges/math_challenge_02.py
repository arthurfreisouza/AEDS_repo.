def Validate(function_):
    def validate(num_):
        if int(num_) < 0:
            raise Exception(' This value is not right')
        else:
            return function_(num_)
    return validate


@Validate
def Factorial_Function(num_ : int) -> int:
    '''
    This function will return the factorial of the number...
    '''
    factorial = 1
    for i in range(num_, 1, -1 ):
        factorial = factorial * i
    
    return factorial


for i in range(100000000):
    sum_result = 0

    for digit_char in str(i):
        digit = int(digit_char)
        sum_result = sum_result + Factorial_Function(int(digit))
        
    if int(sum_result) == int(i):
        print('The value {} is a curious number. '.format(i))
        with open('/home/arthur/Desktop/result_file.txt', 'a') as file:
            file.write('The value {} is a curious number. '.format(i))
        del file

    